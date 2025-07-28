import heapq

# Goal state for reference
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Moves: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class PuzzleState:
    def __init__(self, board, moves_count=0, previous=None):
        self.board = board
        self.moves_count = moves_count
        self.previous = previous
        self.priority = self.moves_count + self.heuristic()

    def __lt__(self, other):
        return self.priority < other.priority

    def heuristic(self):
        """Manhattan Distance"""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    goal_i, goal_j = divmod(value - 1, 3)
                    distance += abs(goal_i - i) + abs(goal_j - j)
        return distance

    def get_neighbors(self):
        neighbors = []
        x, y = next((i, j)
                    for i in range(3)
                    for j in range(3)
                    if self.board[i][j] == 0)

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                # Swap 0 with the target tile
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self.moves_count + 1, self))
        return neighbors

    def is_goal(self):
        return self.board == goal_state

    def __hash__(self):
        return hash(str(self.board))

    def __eq__(self, other):
        return self.board == other.board

    def print_path(self):
        path = []
        state = self
        while state:
            path.append(state.board)
            state = state.previous
        for step in reversed(path):
            for row in step:
                print(row)
            print('---')

def a_star(start_board):
    start_state = PuzzleState(start_board)
    frontier = []
    heapq.heappush(frontier, start_state)
    visited = set()

    while frontier:
        current = heapq.heappop(frontier)
        if current.is_goal():
            print("Goal reached in", current.moves_count, "moves!")
            current.print_path()
            return

        visited.add(hash(current))

        for neighbor in current.get_neighbors():
            if hash(neighbor) not in visited:
                heapq.heappush(frontier, neighbor)

    print("No solution found.")

# Example usage
start_board = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

a_star(start_board)
