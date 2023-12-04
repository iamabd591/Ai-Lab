from heapq import heappush, heappop

def heuristic(node, goal):
    return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

def astar(graph, start, goal):
    open_set = [(0 + heuristic(start, goal), 0, start, [])]

    while open_set:
        _, cost, current, path = heappop(open_set)

        if current == goal:
            return path + [current]

        for neighbor, step_cost in graph[current]:
            new_cost = cost + step_cost
            heappush(open_set, (new_cost + heuristic(neighbor, goal), new_cost, neighbor, path + [current]))

    return None 
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((0, 1), 1), ((1, 0), 1)]
}

start_node = (0, 0)
end_node = (1, 1)

result = astar(graph, start_node, end_node)

if result:
    print(f"Path from {start_node} to {end_node}: {result}")
else:
    print(f"No path found from {start_node} to {end_node}")
