import random

def generate_taci_file(filename, n):

    numbers = list(range(n**2))

    # Trộn ngẫu nhiên danh sách các số
    random.shuffle(numbers)

    # Ghi vào file
    with open(filename, 'w') as file:
        # Ghi số n vào dòng đầu tiên
        file.write(str(n) + '\n')

        # Ghi các số vào các dòng tiếp theo
        for i in range(n):
            # Lấy n số từ danh sách đã trộn
            row_numbers = numbers[i*n : (i+1)*n]

            # Ghi n số vào một dòng, cách nhau bằng khoảng trắng
            row_str = ' '.join(str(num) for num in row_numbers)
            file.write(row_str + '\n')

# n = random.randint(3, 99)
n = 3

# Gọi hàm để tạo file
generate_taci_file('taci.txt', n)