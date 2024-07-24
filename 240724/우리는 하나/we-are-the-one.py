from itertools import combinations
from collections import deque

def is_within_bounds(x, y, n):
    return 0 <= x < n and 0 <= y < n

def bfs(start_x, start_y, grid, n, u, d, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_within_bounds(nx, ny, n) and (nx, ny) not in visited:
                height_diff = abs(grid[x][y] - grid[nx][ny])
                if u <= height_diff <= d:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    count += 1
    
    return count

def solution(n, k, grid, u, d):
    max_reachable = 0
    all_positions = [(i, j) for i in range(n) for j in range(n)]
    
    for positions in combinations(all_positions, k):
        visited = set()
        total_reachable = 0
        for x, y in positions:
            if (x, y) not in visited:
                total_reachable += bfs(x, y, grid, n, u, d, visited)
        
        max_reachable = max(max_reachable, total_reachable)
    
    return max_reachable

n, k, u, d = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]

result = solution(n, k, graph, u, d)
print(result)