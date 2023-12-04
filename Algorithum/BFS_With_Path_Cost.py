from collections import deque

def BFS(graph, start, end):
    visited = set()
    queue = deque([(start, [start], 0)])  
    while queue:
        current_node, path, cost = queue.popleft()

        if current_node == end:
            print(f"Path from {start} to {end}: {' -> '.join(path)}")
            print(f"Total Cost: {cost}")
            return

        if current_node not in visited:
            visited.add(current_node)

            for next_node, edge_cost in graph[current_node]:
                if next_node not in visited:
                    new_path = path + [next_node]
                    queue.append((next_node, new_path, cost + edge_cost))

    print(f"No path found from {start} to {end}")

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
BFS(graph_with_cost, start_node, end_node)
