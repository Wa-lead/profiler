import line_profiler
import sys
import os
import importlib.util
import inspect  # Import the inspect module to check function source

def profile_script(script_path):
    # Ensure the script exists
    if not os.path.isfile(script_path):
        print(f"Error: {script_path} does not exist.")
        return

    # Adjust the Python path and working directory
    script_dir = os.path.dirname(script_path) or '.'  # Use '.' if the dirname is empty
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    
    # Change the current working directory safely
    try:
        os.chdir(script_dir)
    except Exception as e:
        print(f"Error changing to directory {script_dir}: {e}")
        return

    # Dynamically import the script as a module
    script_name = os.path.splitext(os.path.basename(script_path))[0]
    spec = importlib.util.spec_from_file_location(script_name, script_path)
    script_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script_module)

    # Create a LineProfiler instance
    profiler = line_profiler.LineProfiler()

    # Get the absolute path of the script for comparison
    abs_script_path = os.path.abspath(script_path)

    # Add only functions defined in the script to the profiler
    for name, obj in vars(script_module).items():
        if callable(obj) and inspect.isfunction(obj):
            # Check if the function is defined in the target script
            if inspect.getsourcefile(obj) == abs_script_path:
                profiler.add_function(obj)

    # Attempt to execute the main block by inferring the entry point
    if hasattr(script_module, 'main'):
        print("Profiling 'main' function...")
        profiler.enable_by_count()  # Start profiling
        try:
            script_module.main()  # Execute the main function
        finally:
            profiler.disable_by_count()  # Stop profiling
    else:
        print("No 'main' function found. Profiling all functions without explicit execution.")

    # Print the profiling results
    profiler.print_stats()

def main():
    if len(sys.argv) != 2:
        print("Usage: python profile_script.py script_to_profile.py")
    else:
        profile_script(sys.argv[1])
        
        
if __name__ == "__main__":
    main()