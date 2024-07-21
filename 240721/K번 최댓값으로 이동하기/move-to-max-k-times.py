import copy

def solution(n, k, position, arr):


    def bfs(x, y, graph):
        stack = [(x, y)]
        indexStack = []
        maxNum = graph[x][y]
        curMax = 0
        first = True
        if n==1:
            first = False

        while stack:
            cx, cy = stack.pop()
            if graph[cx][cy] > curMax and not first:
                curMax = graph[cx][cy]
                indexStack.clear()
                indexStack.append((cx, cy))
            if graph[cx][cy] == curMax and not first:
                indexStack.append((cx, cy))
            first = False
            if graph[cx][cy] == 0:
                continue

            graph[cx][cy] = 0
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in direction:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] < maxNum:
                    stack.append((nx, ny))
        if indexStack:
            indexStack.sort(key=lambda x: (x[0], x[1]))
            return indexStack[0]
        else:
            return (x, y)
    
    arr2 = copy.deepcopy(arr)
    x, y = bfs(position[0] - 1, position[1] - 1, arr2)
    for i in range(k-1):
        arr2 = copy.deepcopy(arr)
        x, y = bfs(x, y, arr2)
    return [x+1,y+1]


n, k = map(int, input().split())
numbers = []
graph = []

for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
position = list(map(int, input().split()))

numbers.sort()
result = solution(n, k, position, graph)
print(*result)