from collections import deque


def BFS(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
             print(node, end=' ')
             visited.add(node)
             queue.extend(nodes for nodes in graph[node] if nodes not in visited)

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

start_node = 'A'
print("BFS traversal starting from node", start_node, ":")
BFS(graph, start_node)