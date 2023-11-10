def read_graph_from_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()
        n = int(lines[0])
        graph = [[int(x) for x in line.split()] for line in lines[1:]]
    return n, graph

def welch_powell_coloring(graph):
    # Đếm số đỉnh trong đồ thị
    num_vertices = len(graph)
    
    # Khởi tạo danh sách kề cho từng đỉnh
    adjacency_list = [[] for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                adjacency_list[i].append(j)

    # Khởi tạo mảng màu cho từng đỉnh, ban đầu tất cả đỉnh chưa được tô màu (-1)
    colors = [-1] * num_vertices

    # Sắp xếp các đỉnh theo số đỉnh kề đã tô màu giảm dần
    vertices_degree = [(vertex, len(adjacency_list[vertex])) for vertex in range(num_vertices)]
    vertices_degree.sort(key=lambda x: x[1], reverse=True)

    # Bắt đầu tô màu
    num_colors = 0
    for vertex, _ in vertices_degree:
        # Tạo danh sách màu đã sử dụng bởi các đỉnh kề
        used_colors = set(colors[neighbor] for neighbor in adjacency_list[vertex] if colors[neighbor] != -1)

        # Tìm màu chưa sử dụng cho đỉnh hiện tại
        for color in range(num_colors + 1):
            if color not in used_colors:
                colors[vertex] = color
                num_colors = max(num_colors, color)
                break
    
    return colors, num_colors + 1

# Example usage:
if __name__ == "__main__":
    # Đồ thị mẫu, 1 là có kết nối, 0 là không kết nối
    graph = read_graph_from_file("./TH4/color2.txt")

    colors, num_colors = welch_powell_coloring(graph)

    print("Màu của từng đỉnh:")
    for i, color in enumerate(colors):
        print(f"Đỉnh {i}: Màu {color}")

    print(f"Tổng số màu cần: {num_colors}")
