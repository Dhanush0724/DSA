from collections import deque

def floodFill(image, sr, sc, color):
    initial_color = image[sr][sc]
    
    if initial_color == color:
        return image
    
    rows, cols = len(image), len(image[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    queue = deque([(sr, sc)])
    
    while queue:
        r, c = queue.popleft()
        if image[r][c] == initial_color:
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == initial_color:
                    queue.append((nr, nc))
    
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc = 1, 1
color = 2
print(floodFill(image, sr, sc, color))
