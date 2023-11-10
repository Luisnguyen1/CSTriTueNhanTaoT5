import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.g_score = float('inf')
        self.f_score = float('inf')
        self.neighbors = []
        self.previous = None
    
    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))

def read_graph_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        n, m = map(int, lines[0].split())
        s, t = map(int, lines[1].split())
        
        graph = {}
        for line in lines[2:]:
            u, v, weight = map(int, line.split())
            if u not in graph:
                graph[u] = Node(u, 0)
            if v not in graph:
                graph[v] = Node(v, 0)
            graph[u].add_neighbor(graph[v], weight)
        
        return graph, n, s, t

def astar(graph, n, start, goal):
    start_node = graph[start]
    start_node.g_score = 0
    start_node.f_score = start_node.heuristic
    
    open_set = [(start_node.f_score, start_node)]
    closed_set = set()
    
    while open_set:
        current_f_score, current_node = heapq.heappop(open_set)
        
        if current_node.name == goal:
            return reconstruct_path(current_node)
        
        closed_set.add(current_node)
        
        for neighbor, weight in current_node.neighbors:
            if neighbor in closed_set:
                continue
            
            tentative_g_score = current_node.g_score + weight
            
            if tentative_g_score < neighbor.g_score:
                neighbor.previous = current_node
                neighbor.g_score = tentative_g_score
                neighbor.f_score = tentative_g_score + neighbor.heuristic
                
                if neighbor not in [node for _, node in open_set]:
                    heapq.heappush(open_set, (neighbor.f_score, neighbor))
    
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.previous
    return list(reversed(path))

# Đọc và xử lý dữ liệu đầu vào
graph, n, start, goal = read_graph_file('graph1.txt')

# Chạy thuật toán A*
result = astar(graph, n, start, goal)

# In ra kết quả
if result:
    print("Đường đi ngắn nhất:", result)
    print("Chiều dài của đường đi:", graph[goal].g_score)
else:
    print("Không tìm thấy đường đi từ", start, "đến", goal)