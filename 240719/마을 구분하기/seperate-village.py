def solution(n, arr):
    global count
    def dfs(x, y):
        global count
        count += 1
        arr[x][y] = 0
        if x + 1 < n and arr[x + 1][y] == 1:
            dfs(x + 1, y)
        if x - 1 > -1 and arr[x - 1][y] == 1:
            dfs(x - 1, y)
        if y + 1 < n and arr[x][y + 1] == 1:
            dfs(x, y + 1)
        if y - 1 > -1 and arr[x][y - 1] == 1:
            dfs(x, y - 1)

    re = []
    for i in range(n):  # 'N' 대신 'n' 사용
        for j in range(n):  # 'N' 대신 'n' 사용
            if arr[i][j] == 1:
                count = 0
                dfs(i, j)
                re.append(count)
    re.sort()  # 리스트를 정렬
    return re  # 정렬된 리스트 반환

count = 0
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = solution(N, graph)
print(len(result))
for value in result:  # 'i' 대신 'value' 사용
    print(value)