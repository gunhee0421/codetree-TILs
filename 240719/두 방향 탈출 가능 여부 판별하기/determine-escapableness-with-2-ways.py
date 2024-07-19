n, m = map(int, input().split())
graph = []
result = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

def dfs(y, x):
    global result
    if (y==n-1 and x ==m-1):
        result = 1
        return

    graph[y][x] = 0

    if (x+1 < m and graph[y][x+1] != 0):
        dfs(y, x+1)
    if (y+1 < n and graph[y+1][x] != 0):
        dfs(y+1, x)


dfs(0, 0)
print(result)