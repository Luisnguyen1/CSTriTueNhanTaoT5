import random

def generate_random_file(filename):
    n = random.randint(3, 3)  # Số đĩa nằm trong khoảng từ 3 đến 16
    towers = ['A', 'B', 'C']  # Tên các cột

    # Tạo danh sách số hiệu đĩa và danh sách các cột
    disks = list(range(1, n + 1))
    random.shuffle(disks)
    random.shuffle(towers)

    # Tạo ma trận kết quả ban đầu
    result = [['0'] * n for _ in range(3)]

    # Đặt các đĩa vào các cột một cách ngẫu nhiên
    for i in range(n):
        tower = random.choice(towers)
        result[towers.index(tower)][i] = str(disks[i])

    # Kiểm tra và thay thế các cột không có đĩa bằng số 0
    for i in range(3):
        if all(x == '0' for x in result[i]):
            result[i][0] = '0'

    # Ghi dữ liệu vào file
    with open(filename, 'w') as file:
        # Ghi số n vào dòng đầu tiên
        file.write(str(n) + '\n')

        # Ghi ma trận kết quả vào file
        for row in result:
            row = [x for x in row if x != '0']
        
        for i in range(3):
            if all(x == '' for x in result[i]):
                result[i][0] = '0'
        
        for row in result:
            new_row = []
            i = 1
            for x in row:
                if x != '0':
                    new_row.append(x)
                i+=1
            i = 0
            row = new_row
            line = ' '.join(row)
            file.write(line + '\n')

    print(f"Đã tạo file '{filename}' thành công.")

# Tạo file ngẫu nhiên
generate_random_file('HNtower.txt')