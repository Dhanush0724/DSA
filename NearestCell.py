from collections import deque
def nearest_one_distance(grid):
    if not grid or not grid[0]:
        return []
    
    rows,cols = len(grid),len(grid[0])
    distance = [[float('inf')]*cols for _ in range(rows)]
    visited = [[0]*cols for _ in range(rows)]
    queue = deque()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                queue.append((r,c))
                distance[r][c] = 0
                visited[r][c] = 1

    directions =   [(0,1),(0,-1),(1,0),(-1,0)]

    while queue:
        r,c = queue.popleft()
        for dr,dc in directions:
            nr,nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc]:
                distance[nr][nc] = distance[r][c] +1
                visited[nr][nc] = 1
                queue.append((nr,nc))
    return distance




    

grid = [
    [0,0,0],
    [0,1,0],
    [1,0,0]
]

result = nearest_one_distance(grid)
for row in result:
    print(row)