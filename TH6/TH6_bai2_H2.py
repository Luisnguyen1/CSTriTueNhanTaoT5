def heuristic_H2(board, goal_board):
    mismatch_count = 0
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] != goal_board[i][j]:
                mismatch_count += 1
    return mismatch_count

# Đọc dữ liệu từ file
with open('taci5.txt', 'r') as file:
    n = int(file.readline().strip())
    start_board = [list(map(int, file.readline().split())) for _ in range(n)]
    goal_board = [list(map(int, file.readline().split())) for _ in range(n)]

# Tính giá trị độ đo ước lượng H2
h2_value = heuristic_H2(start_board, goal_board)

# In ra giá trị độ đo ước lượng H2
print("Giá trị độ đo ước lượng H2:", h2_value)