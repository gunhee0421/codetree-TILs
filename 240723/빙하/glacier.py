from collections import deque
import enum

class Element(enum.Enum):
    WATER = 0
    GLACIER = 1
    
n, m = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

q = deque()
glaciers_to_melt = deque()
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
cnt = 0

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

elapsed_time = 0
last_melt_cnt = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    return in_range(x, y) and a[x][y] == Element.WATER.value and not visited[x][y]


def is_glacier(x, y):
    return in_range(x, y) and a[x][y] == Element.GLACIER.value and not visited[x][y]


def initialize():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            
def bfs():

    initialize()
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True

def outside_water_exist_in_neighbor(x, y):
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if in_range(new_x, new_y) and visited[new_x][new_y]:
            return True
        
    return False

def melt():
    global last_melt_cnt
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == Element.GLACIER.value and \
                    outside_water_exist_in_neighbor(i, j):
                a[i][j] = Element.WATER.value
                last_melt_cnt += 1
                
                
def simulate():
    global elapsed_time, last_melt_cnt
    
    elapsed_time += 1
    last_melt_cnt = 0
    
    bfs()
    
    melt()
    
def glacier_exist():
    for i in range(n):
        for j in range(m):
            if a[i][j] == Element.GLACIER.value:
                return True
    return False


while True:
    simulate()
        if not glacier_exist():
        break
        
print(elapsed_time, last_melt_cnt)