import heapq

class State:
    def __init__(self, board, goal, cost, parent=None, move=None):
        self.board = board
        self.goal = goal
        self.cost = cost
        self.parent = parent
        self.move = move

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

#tính hàm H
def get_manhattan_distance(board, goal, goal_position_map):
    distance = 0
    size = len(board)
    for i in range(size):
        for j in range(size):
            value = board[i][j]
            if value != 0:
                goal_position = goal_position_map[value]
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
    return distance

#kiểm tra nước đi có thể đi
def get_possible_moves(board):
    size = len(board)
    moves = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                if i > 0:
                    moves.append((i - 1, j))  # Up
                if i < size - 1:
                    moves.append((i + 1, j))  # Down
                if j > 0:
                    moves.append((i, j - 1))  # Left
                if j < size - 1:
                    moves.append((i, j + 1))  # Right
    return moves

def apply_move(board, move):
    i, j = move
    new_board = [row.copy() for row in board]
    zero_i, zero_j = get_zero_position(board)
    new_board[zero_i][zero_j] = board[i][j]
    new_board[i][j] = 0
    return new_board

def get_zero_position(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == 0:
                return i, j

def print_path(state):
    path = []
    current = state
    while current is not None:
        path.append(current.board)
        current = current.parent
    path.reverse()
    for board in path:
        for row in board:
            print(row)
        print()

def solve_taci(start_board, goal_board):
    size = len(start_board)
    start_state = State(start_board, goal_board, 0)
    goal_state = State(goal_board, goal_board, float('inf'))
    goal_position_map = {}
    for i in range(size):
        for j in range(size):
            goal_position_map[goal_board[i][j]] = (i, j)

    open_set = []
    closed_set = set()

    heapq.heappush(open_set, start_state)

    while open_set:
        current_state = heapq.heappop(open_set)
        current_board = current_state.board

        if current_state == goal_state:
            print("Có cách giải")
            print_path(current_state)
            return

        closed_set.add(current_state)

        possible_moves = get_possible_moves(current_board)
        for move in possible_moves:
            new_board = apply_move(current_board, move)
            new_state_cost = current_state.cost + 1
            new_state = State(new_board, goal_board, new_state_cost, current_state, move)
            if new_state in closed_set:
                continue

            new_state.cost += get_manhattan_distance(new_board, goal_board, goal_position_map)
            heapq.heappush(open_set, new_state)

    print("Không có cách giải !")

# Bàn chơi ban đầu
with open('taci1.txt', 'r') as file:
    n = int(file.readline().strip())
    start_board = [list(map(int, file.readline().split())) for _ in range(n)]
    goal_board = [list(map(int, file.readline().split())) for _ in range(n)]
    

solve_taci(start_board, goal_board)