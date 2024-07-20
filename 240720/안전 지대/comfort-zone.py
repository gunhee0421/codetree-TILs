import copy

def solution(k, graph):
    count=0
    copyGraph = copy.deepcopy(graph)
    n = len(copyGraph)
    m = len(copyGraph[0])

    for i in range(len(copyGraph)):
        for j in range(len(copyGraph[i])):
            if copyGraph[i][j] <= k:
                copyGraph[i][j] = 0 

    def dfs(x, y):
        copyGraph[x][y] = 0
        if x + 1 < n and copyGraph[x + 1][y] > 0:
            dfs(x + 1, y)
        if x - 1 > -1 and copyGraph[x - 1][y] > 0:
            dfs(x - 1, y)
        if y + 1 < m and copyGraph[x][y + 1] > 0:
            dfs(x, y + 1)
        if y - 1 > -1 and copyGraph[x][y - 1] > 0:
            dfs(x, y - 1)
    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] > 0:
                count+=1
                dfs(i, j)
    return count

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

minN = min(map(min, graph))
maxN = max(map(max, graph))

result = [1, 0]
for i in range(1, maxN):
    ans = solution(i, graph)
    if ans > result[1]:
        result[0] = i
        result[1] = ans
print(*result)