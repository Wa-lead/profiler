# Profiler

Profiler is an extremely friendly Python package designed for profiling Python scripts to analyze their runtime performance with a focus on line-by-line analysis. It leverages the `line_profiler` package to give developers insights into which lines of code consume the most time, helping to optimize and improve code efficiency.

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
> NOTE: script.py must have a `main()` function.

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

run:

```
profiler example.py
```

output:

```
Profiling 'main' function...
Timer unit: 1e-09 s

Total time: 1e-06 s
File: /Users/waleedalasad/Documents/GitHub/profiler/test.py
Function: func at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def func(a,b):
     2         1       1000.0   1000.0    100.0      return a+b

Total time: 3e-06 s
File: /Users/waleedalasad/Documents/GitHub/profiler/test.py
Function: main at line 5

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     5                                           def main():
     6         1       1000.0   1000.0     33.3      a = 1
     7         1          0.0      0.0      0.0      b = 2
     8         1       2000.0   2000.0     66.7      c = func(a,b)

(base) MITL0218:profiler waleedalasad$ profiler test.py
Profiling 'main' function...
Found a coloring: {0: 'Red', 1: 'Green', 2: 'Blue', 3: 'Green', 4: 'Red'}
Timer unit: 1e-09 s

Total time: 1.4e-05 s
File: /Users/waleedalasad/Documents/GitHub/profiler/test.py
Function: is_valid at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def is_valid(coloring, graph, node, color):
     2        26       5000.0    192.3     35.7      for neighbor in graph[node]:
     3        21       7000.0    333.3     50.0          if color == coloring.get(neighbor):
     4         4       1000.0    250.0      7.1              return False
     5         5       1000.0    200.0      7.1      return True

Total time: 2.6e-05 s
File: /Users/waleedalasad/Documents/GitHub/profiler/test.py
Function: color_map at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def color_map(graph, colors, node=0, coloring={}):
     8         6       2000.0    333.3      7.7      if node == len(graph):
     9         1          0.0      0.0      0.0          return coloring
    10                                           
    11         9       1000.0    111.1      3.8      for color in colors:
    12         9      21000.0   2333.3     80.8          if is_valid(coloring, graph, node, color):
    13         5       1000.0    200.0      3.8              coloring[node] = color
    14         5          0.0      0.0      0.0              result = color_map(graph, colors, node + 1, coloring)
    15         5       1000.0    200.0      3.8              if result is not None:
    16         5          0.0      0.0      0.0                  return coloring
    17                                                       del coloring[node]
    18                                           
    19                                               return None

Total time: 4.7e-05 s
File: /Users/waleedalasad/Documents/GitHub/profiler/test.py
Function: main at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           def main():
    22                                               # Define the map as a graph: node numbers represent regions, edges represent adjacencies.
    23         1       1000.0   1000.0      2.1      graph = {
    24         1       1000.0   1000.0      2.1          0: [1, 2, 3],
    25         1          0.0      0.0      0.0          1: [0, 2, 4],
    26         1          0.0      0.0      0.0          2: [0, 1, 3, 4],
    27         1          0.0      0.0      0.0          3: [0, 2, 4],
    28         1          0.0      0.0      0.0          4: [1, 2, 3]
    29                                               }
    30         1          0.0      0.0      0.0      colors = ['Red', 'Green', 'Blue', 'Yellow']  # Define available colors
    31                                           
    32         1      39000.0  39000.0     83.0      coloring = color_map(graph, colors)
    33         1          0.0      0.0      0.0      if coloring is not None:
    34         1       6000.0   6000.0     12.8          print("Found a coloring:", coloring)
    35                                               else:
    36                                                   print("No coloring found that satisfies all constraints.")
```


Make sure `example.py` has a `main()` function defined, as Profiler will attempt to profile this function.
