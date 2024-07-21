def solution(n, m, graph):
    stack = [(0, 0)]

    while stack:
        cx, cy = stack.pop()
        if graph[cx][cy] == 0:
            continue
        graph[cx][cy]=0
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx, dy in direction:
            nx, ny = cx + dx, cy +dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                stack.append((nx, ny))
    
    if graph[n-1][m-1] == 1:
        return 0
    else:
        return 1
    

n, m =map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, m, graph))