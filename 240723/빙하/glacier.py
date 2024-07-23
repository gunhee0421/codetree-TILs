from collections import deque

def melt_glacier(n, m, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_within_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    def add_to_queue_if_boundary(x, y, queue, visited):
        if is_within_bounds(x, y) and (x, y) not in visited and grid[x][y] == 0:
            visited.add((x, y))
            queue.append((x, y))

    time = 0
    last_melt_size = 0
    
    water_boundary = deque()
    visited = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and (i == 0 or i == n-1 or j == 0 or j == m-1):
                water_boundary.append((i, j))
                visited.add((i, j))

    while True:
        to_melt = set()
        new_water_boundary = set()

        for _ in range(len(water_boundary)):
            x, y = water_boundary.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_within_bounds(nx, ny):
                    if grid[nx][ny] == 1:
                        to_melt.add((nx, ny))
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        water_boundary.append((nx, ny))

        if not to_melt:
            break
        
        last_melt_size = len(to_melt)
        for x, y in to_melt:
            grid[x][y] = 0
            add_to_queue_if_boundary(x, y, water_boundary, visited)

        time += 1

    return time, last_melt_size

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

time, last_melt_size = melt_glacier(n, m, grid)
print(time, last_melt_size)