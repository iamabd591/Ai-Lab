from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    explored = set()
    path = {start: None}
    
    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            return construct_path(path, start, goal)
        for neighbor in graph[current_node]:
            if neighbor not in explored:
                queue.append(neighbor)
                explored.add(neighbor)
                path[neighbor] = current_node
    return None

def construct_path(path, start, goal):
    current_node = goal
    path_list = [current_node]
    while current_node != start:
        current_node = path[current_node]
        path_list.insert(0, current_node)
    return path_list

graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'E', 'F'],
    'C': ['A'],
    'D': ['A', 'G'],
    'E': ['B'],
    'F': ['B', 'G'],
    'G': ['D', 'F']
}

start_node = 'S'
goal_node = 'G'
result_path = bfs(graph, start_node, goal_node)

if result_path:
    print(f"Path from {start_node} to {goal_node}: {result_path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
