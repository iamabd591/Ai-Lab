def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def dfs_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, end, path)
            if new_path:
                return new_path

    return None

def coastal(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]

        if next_node in graph[current_node]:
            # Assuming the graph contains the cost of the edge
            edge_cost = graph[current_node][next_node]
            cost += edge_cost
        else:
            # If the edge is not present in the graph, handle the case accordingly
            print(f"Edge not found between {current_node} and {next_node}")

    return cost

# Example graph
example_graph = {
    0: {1: 1, 3: 2},
    1: {0: 1, 2: 3, 3: 4, 4: 5},
    2: {1: 3, 4: 6},
    3: {0: 2, 1: 4, 5: 7},
    4: {1: 5, 2: 6, 8: 8},
    5: {3: 7, 6: 9},
    6: {5: 9, 8: 10},
    8: {4: 8, 6: 10}
}

# i. DFS Method
print("DFS traversal starting from node 0:")
dfs(example_graph, 0)
print("\n")

# ii. DFS-Based Path Method
start_node = 1
end_node = 4
path_result = dfs_path(example_graph, start_node, end_node)
print(f"DFS-based path from {start_node} to {end_node}: {path_result}")
print("\n")

# iii. Coastal Function
path1 = [1, 2, 4, 8]
path2 = [0, 1, 3, 5, 6]

cost1 = coastal(example_graph, path1)
cost2 = coastal(example_graph, path2)

print(f"Cost of path {path1}: {cost1}")
print(f"Cost of path {path2}: {cost2}")
