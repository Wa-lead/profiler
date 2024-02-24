# Profiler

Profiler is an extremely user-friendly Python package designed for profiling Python scripts to analyze their runtime performance with a focus on line-by-line analysis. It leverages the `line_profiler` package to give developers insights into which lines of code consume the most time, helping to optimize and improve code efficiency.

## Installation

To install Profiler, simply use pip:

```
pip install git+https://github.com/wa-lead/profiler.git
```

## Usage

After installation, you can use the `profiler` command followed by your script's filename to profile it:

```
profiler script.py
```

This will run `script.py` and output a line-by-line breakdown of execution time.

### Function Selection

If you want to selectively profile specific functions within your script, you can use the `--select` option to interactively choose which functions to profile:

```
profiler script.py --select
```

Upon using this command, you'll be presented with the list of functions found in `script.py`. 

<img width="1215" alt="Screenshot 2024-02-24 at 4 20 23 PM" src="https://github.com/Wa-lead/profiler/assets/81301826/f86cb759-cbb2-4944-9ce5-ae7f49719029">

> NOTE: `script.py` must have a `main()` function defined, as Profiler will attempt to profile this function.

### Example

Given a Python script `example.py`, you can profile it as follows:

```python
# Description: This is a simple backtracking algorithm to solve the map coloring problem.

def is_valid(coloring, graph, node, color):
    for neighbor in graph[node]:
        if color == coloring.get(neighbor):
            return False
    return True

def color_map(graph, colors, node=0, coloring={}):
    if node == len(graph):
        return coloring

    for color in colors:
        if is_valid(coloring, graph, node, color):
            coloring[node] = color
            result = color_map(graph, colors, node + 1, coloring)
            if result is not None:
                return coloring
            del coloring[node]

    return None

def main():
    # Define the map as a graph: node numbers represent regions, edges represent adjacencies.
    graph = {
        0: [1, 2, 3],
        1: [0, 2, 4],
        2: [0, 1, 3, 4],
        3: [0, 2, 4],
        4: [1, 2, 3]
    }
    colors = ['Red', 'Green', 'Blue', 'Yellow']  # Define available colors

    coloring = color_map(graph, colors)
    if coloring is not None:
        print("Found a coloring:", coloring)
    else:
        print("No coloring found that satisfies all constraints.")

if __name__ == "__main__":
    main()
```

In the terminal, run:

```
profiler example.py
```

or to interactively select functions:

```
profiler example.py --select
```

Output will include a line-by-line breakdown of execution time for each function within `example.py`, helping you identify performance bottlenecks.
