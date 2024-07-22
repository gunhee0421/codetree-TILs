from itertools import combinations

def solution(n, k, m, arr, p):
    def bfs(position, graph):
        visited = [[False]*n for _ in range(n)]
        stack = [(position[0]-1, position[1]-1)]
        # if graph[position[0]-1][position[1]-1] == 1:
        #     return 0
        visited[position[0]-1][position[1]-1] = True
        count=0

        while stack:
            cx, cy = stack.pop()
            count+=1
            direction = [(-1,0),(1,0),(0,1),(0,-1)]
            for dx, dy in direction:
                nx, ny = cx+dx, cy+dy
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny]==0:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        return count

    stone_position = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]
    max_reach = 0

    for i in range(k):
        for stones_to_remove in combinations(stone_position, m):
            grid = [row[:] for row in graph]
            for x, y in stones_to_remove:
                grid[x][y]=0
            reachlen = bfs(p[i], grid)
            max_reach = max(reachlen, max_reach)
    return max_reach


n, k, m = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]
ps = [list(map(int, input().split()))for _ in range(k)]

result = solution(n, k, m, graph, ps)
print(result)