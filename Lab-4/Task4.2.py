from collections import deque

def is_valid(state):
    m_left, c_left, b_left, m_right, c_right, b_right = state
    # Check if the state is valid (no missionaries are eaten)
    return (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right)

def successors(state):
    m_left, c_left, b_left, m_right, c_right, b_right = state
    moves = []

    if b_left == 1:  # Boat is on the left side
        # Move one missionary
        if m_left >= 1:
            moves.append((m_left - 1, c_left, 0, m_right + 1, c_right, 1))
        # Move two missionaries
        if m_left >= 2:
            moves.append((m_left - 2, c_left, 0, m_right + 2, c_right, 1))
        # Move one cannibal
        if c_left >= 1:
            moves.append((m_left, c_left - 1, 0, m_right, c_right + 1, 1))
        # Move two cannibals
        if c_left >= 2:
            moves.append((m_left, c_left - 2, 0, m_right, c_right + 2, 1))
        # Move one missionary and one cannibal
        if m_left >= 1 and c_left >= 1:
            moves.append((m_left - 1, c_left - 1, 0, m_right + 1, c_right + 1, 1))
    else:  # Boat is on the right side
        # Move one missionary
        if m_right >= 1:
            moves.append((m_left + 1, c_left, 1, m_right - 1, c_right, 0))
        # Move two missionaries
        if m_right >= 2:
            moves.append((m_left + 2, c_left, 1, m_right - 2, c_right, 0))
        # Move one cannibal
        if c_right >= 1:
            moves.append((m_left, c_left + 1, 1, m_right, c_right - 1, 0))
        # Move two cannibals
        if c_right >= 2:
            moves.append((m_left, c_left + 2, 1, m_right, c_right - 2, 0))
        # Move one missionary and one cannibal
        if m_right >= 1 and c_right >= 1:
            moves.append((m_left + 1, c_left + 1, 1, m_right - 1, c_right - 1, 0))

    return [move for move in moves if is_valid(move)]

def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()

    while queue:
        state = queue.popleft()
        if state not in visited:
            visited.add(state)
            if state[0] == 0 and state[1] == 0 and state[2] == 0:
                return state  # Goal state reached
            queue.extend(successors(state))

    return None  # No solution found

def dfs(initial_state):
    stack = [initial_state]
    visited = set()

    while stack:
        state = stack.pop()
        if state not in visited:
            visited.add(state)
            if state[0] == 0 and state[1] == 0 and state[2] == 0:
                return state  # Goal state reached
            stack.extend(successors(state)[::-1])

    return None  # No solution found

# Example usage:
initial_state = (3, 3, 1, 0, 0, 0)

print("BFS solution:")
bfs_solution = bfs(initial_state)
print(bfs_solution)

print("\nDFS solution:")
dfs_solution = dfs(initial_state)
print(dfs_solution)
