def solution(n, k, arr):
    an = []
    def bfs(x, y):
        stack = [(x, y)]
        count = 0
        while stack:
            cx, cy = stack.pop()
            if arr[cx][cy] == 1:
                continue
            arr[cx][cy]=1
            count+=1
            direction = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx, dy in direction:
                nx, ny = cx+dx, cy+dy
                if 0<=nx<n and 0<=ny<n and arr[nx][ny]==0:
                    stack.append((nx, ny))
        return count

    for i in range(len(k)):
        an.append(bfs(k[i][0]-1, k[i][1]-1))
    return an

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = [list(map(int, input().split())) for _ in range(k)]

re = sum(solution(n, order, graph))
print(re)