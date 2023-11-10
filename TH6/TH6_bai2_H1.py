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


def heuristic_H2(board, goal_board):
    mismatch_count = 0
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] != goal_board[i][j]:
                mismatch_count += 1
    return mismatch_count
# Bàn chơi ban đầu


with open('taci5.txt', 'r') as file:
    n = int(file.readline().strip())
    start_board = [list(map(int, file.readline().split())) for _ in range(n)]
    goal_board = [list(map(int, file.readline().split())) for _ in range(n)]
    
    
# Tạo goal_position_map cho bàn chơi kết thúc
goal_position_map = {}
size = len(goal_board)
for i in range(size):
    for j in range(size):
        goal_position_map[goal_board[i][j]] = (i, j)

# Tính khoảng cách Manhattan
distance = get_manhattan_distance(start_board, goal_board, goal_position_map)

# In ra khoảng cách Manhattan
print("Khoảng cách H1:", distance)

