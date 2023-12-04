def DFS(graph, start, end, path=None, visited=None, cost=0):
    if path is None:
        path = [start]

    if visited is None:
        visited = set()

    if start == end:
        print(f"Path From {start} to {end}: {' -> '.join(path)}")
        print(f"Total Path Cost is {cost}")
        return

    if start not in visited:
        visited.add(start)
        for nodes, edge_cost in graph[start]:
            if nodes not in visited:
                DFS(graph, nodes, end, path+[nodes], visited, cost+edge_cost)


graph_with_cost = {
    'A': [('B', 1), ('C', 2)],
    'B': [('A', 1), ('D', 3), ('E', 4)],
    'C': [('A', 2), ('F', 1), ('G', 2)],
    'D': [('B', 3)],
    'E': [('B', 4), ('H', 5)],
    'F': [('C', 1)],
    'G': [('C', 2)],
    'H': [('E', 5)]
}

start_node = 'A'
end_node = 'H'

print(f"Finding path from {start_node} to {end_node}:")
DFS(graph_with_cost, start_node, end_node)
