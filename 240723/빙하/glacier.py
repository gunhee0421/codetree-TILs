from collections import deque

def melt_glacier(n, m, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_within_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    def find_initial_water_boundary():
        boundary = set()
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i == 0 or i == n-1 or j == 0 or j == m-1):
                    queue.append((i, j))
                    boundary.add((i, j))
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_within_bounds(nx, ny) and grid[nx][ny] == 0 and (nx, ny) not in boundary:
                    boundary.add((nx, ny))
                    queue.append((nx, ny))
        
        return boundary

    def melt_and_update_boundary(boundary):
        to_melt = set()
        new_boundary = set()

        for x, y in boundary:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_within_bounds(nx, ny):
                    if grid[nx][ny] == 1:
                        to_melt.add((nx, ny))
                    elif grid[nx][ny] == 0:
                        new_boundary.add((nx, ny))

        for x, y in to_melt:
            grid[x][y] = 0
            new_boundary.add((x, y))
        
        return to_melt, new_boundary

    time = 0
    last_melt_size = 0
    water_boundary = find_initial_water_boundary()

    while True:
        to_melt, new_boundary = melt_and_update_boundary(water_boundary)
        
        if not to_melt:
            break
        
        last_melt_size = len(to_melt)
        water_boundary = new_boundary
        time += 1

    return time, last_melt_size

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

time, last_melt_size = melt_glacier(n, m, grid)
print(time, last_melt_size)