from itertools import combinations
from collections import deque

def width_bound(x, y, n):
    return 0<=x<n and 0<=y<n

def bfs(x, y, graph, n, u, d):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False] * n for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx,ny = cx+dx, cy+dy
            if width_bound(nx, ny, n) and not visited[nx][ny]:
                height_diff = abs(graph[cx][cy] - graph[nx][ny])
                if u<=height_diff<=d:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    count+=1
    return count

def solution(n, k, grid, u, d):
    max_reachable = 0
    all_position = [(i,j) for i in range(n) for j in range(n)]

    for positions in combinations(all_position, k):
        total_reachable = 0
        visited_position = set()
        for cx,cy in positions:
            if (cx,cy) not in visited_position:
                reachable = bfs(cx, cy, grid, n, u, d)
                total_reachable += reachable
                visited_position.add((cx,cy))
        max_reachable = max(max_reachable, total_reachable)
    return max_reachable

n, k, u, d = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]

result = solution(n, k, graph, u, d)
print(result)