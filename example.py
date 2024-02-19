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
