# Функция для добавления вершин в граф
def add_edge(gr, u, v):
    if u not in gr:
        graph[u] = []
    if v not in gr:
        graph[v] = []
    gr[u].append(v)
    gr[v].append(u)

# Функция для обхода графа в глубину
def dfs(gr, current, destination, visited=None, depth=0):
    if visited is None:
        visited = set()
    if current == destination:
        return True, depth
    visited.add(current)
    for next_node in graph[current]:
        if next_node not in visited:
            fnd, d = dfs(gr, next_node, destination, visited, depth+1)
            if fnd:
                return True, d
    return False, 0

# Пример использования
graph = {}
add_edge(graph, 4, 2)
add_edge(graph, 1, 3)
add_edge(graph, 2, 4)

start_vertex = 2
end_vertex = 4
found, path_length = dfs(graph, start_vertex, end_vertex)

if found:
    print(f"Длина пути от {start_vertex} до {end_vertex}: {path_length}")
else:
    print(f"Путь от {start_vertex} до {end_vertex} не найден.")