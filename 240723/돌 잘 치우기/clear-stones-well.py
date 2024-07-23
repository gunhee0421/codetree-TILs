from itertools import combinations

def solution(n, k, m, graph, ps):
    def bfs(start_positions, graph):
        visited = [[False] * n for _ in range(n)]
        queue = []
        for position in start_positions:
            x, y = position[0] - 1, position[1] - 1
            queue.append((x, y))
            visited[x][y] = True
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        reach_count = 0
        
        while queue:
            cx, cy = queue.pop(0)
            reach_count += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        
        return reach_count

    stone_positions = [(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]
    max_reach = 0

    for stones_to_remove in combinations(stone_positions, m):
        temp_graph = [row[:] for row in graph]
        for x, y in stones_to_remove:
            temp_graph[x][y] = 0
        max_reach = max(max_reach, bfs(ps, temp_graph))

    return max_reach

n, k, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ps = [list(map(int, input().split())) for _ in range(k)]

result = solution(n, k, m, graph, ps)
print(result)