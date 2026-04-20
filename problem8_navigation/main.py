from collections import deque

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

# BFS
def bfs(start, goal):
    visited = []
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            if node == goal:
                return path

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

            visited.append(node)

# DFS
def dfs(start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return path

    for node in graph[start]:
        if node not in path:
            newpath = dfs(node, goal, path)
            if newpath:
                return newpath

print("BFS Path:", bfs('A', 'F'))
print("DFS Path:", dfs('A', 'F'))
