def add_edge(gr, u, v):
    if u not in gr:
        gr[u] = []
    if v not in gr:
        gr[v] = []
    gr[u].append(v)
    gr[v].append(u)


def dfs(gr, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next_node in gr[start]:
        if next_node not in visited:
            dfs(gr, next_node, visited)
    return

# Пример создания графа и вызова функции обхода
graph = {}
add_edge(graph, 4, 2)
add_edge(graph, 1, 3)
add_edge(graph, 2, 4)  # Это ребро уже добавлено из предыдущего добавления, но повтор не влияет

start_vertex = 1
print("Путь обхода: ")
dfs(graph, start_vertex)