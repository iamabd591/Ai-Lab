from heapq import heappush, heappop

def heuristic(node, goal):
    return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

def greedy_best_first_search(graph, start, goal):
    open_set = [(heuristic(start, goal), start, [])]

    while open_set:
        _, current, path = heappop(open_set)

        if current == goal:
            return path + [current]

        for neighbor, _ in graph[current]:
            if neighbor not in path:
                heappush(open_set, (heuristic(neighbor, goal), neighbor, path + [current]))

    return None
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((0, 1), 1), ((1, 0), 1)]
}

start_node = (0, 0)
end_node = (1, 1)

result = greedy_best_first_search(graph, start_node, end_node)

if result:
    print(f"Path from {start_node} to {end_node}: {result}")
else:
    print(f"No path found from {start_node} to {end_node}")
