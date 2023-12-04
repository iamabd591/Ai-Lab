def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for nodes in graph[start]:
            DFS(graph, nodes, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Starting node for DFS
start_node = 'A'

print("DFS traversal starting from node", start_node, ":")
DFS(graph, start_node)
