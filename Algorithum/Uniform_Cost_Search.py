import heapq
def UCS(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)
        
        if current_node not in visited:
            visited.add(current_node)
            path = path+[current_node]

        if current_node == goal:
            print(f"Uniform Cost Search Path From {start} to {goal}:{' -> '.join(path)}")
            print(f"Total Path Cost:{current_cost}")
            return

        for neighbour, neihbour_edge_cost in graph[current_node]:
            if neighbour not in visited:
             heapq.heappush(priority_queue, (current_cost+neihbour_edge_cost, neighbour, path))

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

# Starting and ending neighbour for the search
start_node = 'A'
end_node = 'H'

print(f"Uniform Cost Search from {start_node} to {end_node}:")
UCS(graph_with_cost, start_node, end_node)