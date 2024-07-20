def solution(n, arr):
    result = [0, 0]

    def dfs(x, y, num):
        stack = [(x, y)]
        count = 0
        while stack:
            cx, cy = stack.pop()
            arr[cx][cy] = 0
            count += 1
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in direction:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == num:
                    stack.append((nx, ny))
        return count

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                count = dfs(i, j, arr[i][j])
                if count > 3:
                    result[0] += 1
                    if result[1] < count:
                        result[1] = count

    return result

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = solution(N, graph)
print(*result)