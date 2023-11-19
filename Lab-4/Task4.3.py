def draw_labyrinth(labyrinth, robot_path):
    for i, row in enumerate(labyrinth):
        for j, cell in enumerate(row):
            if (i, j) in robot_path:
                print('.', end=' ')
            else:
                if cell == 0:
                    print('##', end=' ')
                elif cell == 1:
                    print('  ', end=' ')
                elif cell == 2:
                    print('D ', end=' ')
                elif cell == 3:
                    print('K ', end=' ')
        print()

def get_adjacent_passages(labyrinth, x, y):
    adjacent_passages = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < len(labyrinth) and 0 <= new_y < len(labyrinth[0]) and labyrinth[new_x][new_y] == 1:
            adjacent_passages.append((new_x, new_y))

    return adjacent_passages
labyrinth_matrix = [
    [0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 3],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 2]
]

robot_visited = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]

draw_labyrinth(labyrinth_matrix, robot_visited)

x, y = 2, 3
adjacent_passages = get_adjacent_passages(labyrinth_matrix, x, y)
print(f"Adjacent passages to ({x}, {y}): {adjacent_passages}")
