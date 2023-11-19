class PuzzleState:
    def __init__(self, puzzle, moves=0):
        self.puzzle = puzzle
        self.blank_tile = puzzle.index(0)
        self.moves = moves

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(tuple(self.puzzle))

    def get_states(self):
        states = []
        blank_row, blank_col = self.blank_tile // 3, self.blank_tile % 3

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = blank_row + move[0], blank_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_puzzle = list(self.puzzle)
                new_blank_tile = new_row * 3 + new_col
                new_puzzle[self.blank_tile], new_puzzle[new_blank_tile] = new_puzzle[new_blank_tile], new_puzzle[self.blank_tile]
                states.append(PuzzleState(new_puzzle, self.moves + 1))

        return states

initial_state = PuzzleState([1, 2, 3, 4, 5, 6, 0, 7, 8])

final_state = initial_state.get_states()

for states in final_state:
    print(states.puzzle)
