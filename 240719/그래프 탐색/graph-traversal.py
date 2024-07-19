N, M = map(int, input().split())
graph = [[0]*N for _ in range(N)]
nodes = [False]*N
count = 0

for _ in range(M):
    a = list(map(int, input().split()))
    graph[a[0]-1][a[1]-1] = 1
    graph[a[1]-1][a[0]-1] = 1

def dfs(index):
    global count
    nodes[index] = True
    
    for cur in range(N):
        if graph[index][cur]==1 and not nodes[cur]:
            count += 1
            dfs(cur)
dfs(0)

print(count)