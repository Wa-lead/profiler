import line_profiler
import sys
import os
import importlib.util
import inspect
import argparse
import json
import hashlib
try:
    import inquirer
except ImportError:
    print("Inquirer library is not installed. Please install it for interactive functionality.")
    sys.exit(1)


# Define base directory for profiler and cache
PROFILER_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(PROFILER_BASE_DIR, 'cache')

# Ensure the cache directory exists
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def get_cache_filename(script_path):
    """Generate a unique cache filename based on the script path."""
    script_name_hash = hashlib.md5(script_path.encode('utf-8')).hexdigest()
    return os.path.join(CACHE_DIR, f'selections_cache_{script_name_hash}.json')

def save_selections(selections, script_path):
    cache_filename = get_cache_filename(script_path)
    with open(cache_filename, 'w') as f:
        json.dump(selections, f)
        
def load_selections(script_path):
    cache_filename = get_cache_filename(script_path)
    try:
        with open(cache_filename, 'r') as f:
            selections = json.load(f)
            return selections
    except FileNotFoundError:
        return []

def list_functions(script_module, abs_script_path):
    functions = {}
    for name, obj in vars(script_module).items():
        if callable(obj) and inspect.isfunction(obj) and inspect.getsourcefile(obj) == abs_script_path:
            functions[name] = obj
    return functions

def user_select_functions(functions, cached_selections, script_path):
    questions = [
        inquirer.Checkbox('selected',
                          message="Select functions to profile",
                          choices=[name for name in functions.keys()],
                          default=cached_selections),
    ]
    answers = inquirer.prompt(questions)
    save_selections(answers['selected'], script_path)  # Save the current selections for next time
    selected_functions = {name: functions[name] for name in answers['selected']}
    return selected_functions

def profile_script(script_path, select=False):
    script_dir = os.path.dirname(script_path) or '.'
    sys.path.insert(0, script_dir)

    try:
        os.chdir(script_dir)
    except Exception as e:
        print(f"Error changing to directory {script_dir}: {e}")
        return
    try:
        script_path = os.path.abspath(script_path)
        script_name = os.path.splitext(os.path.basename(script_path))[0]
        spec = importlib.util.spec_from_file_location(script_name, script_path)
        script_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(script_module)
    except Exception as e:
        print(f"Cannot find file: {script_name}.py")
        return

    profiler = line_profiler.LineProfiler()
    abs_script_path = os.path.abspath(script_path)
    functions = list_functions(script_module, abs_script_path)

    if select:
        cached_selections = load_selections(script_path)
        functions = user_select_functions(functions, cached_selections, script_path)
    else:
        functions = dict(functions)

    for func in functions.values():
        profiler.add_function(func)

    if hasattr(script_module, 'main'):
        profiler.enable_by_count()
        try:
            script_module.main()
        finally:
            profiler.disable_by_count()
    else:
        print("No 'main' function found. Profiling selected functions without explicit execution.")

    profiler.print_stats()

def main():
    parser = argparse.ArgumentParser(description="Profile a Python script with optional function selection.")
    parser.add_argument("script_path", help="Path to the Python script to profile.")
    parser.add_argument("--select", action="store_true", help="Interactively select functions to profile using cached selections.")
    args = parser.parse_args()

    profile_script(args.script_path, select=args.select)

if __name__ == "__main__":
    main()
