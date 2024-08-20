from collections import deque

class Solution:

    def shortestPath(self, grid, source, destination):
        if source == destination:
            return 0
        
        q = deque([(0, source)])
        n = len(grid)
        m = len(grid[0])

        # Initialize distance matrix correctly
        dist = [[float('inf')] * m for _ in range(n)]
        dist[source[0]][source[1]] = 0

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while q:
            dis, (r, c) = q.popleft()

            for i in range(4):
                newr = r + dr[i]
                newc = c + dc[i]

                # Check if the new cell is within bounds and valid
                if 0 <= newr < n and 0 <= newc < m and grid[newr][newc] == 1 and dis + 1 < dist[newr][newc]:
                    dist[newr][newc] = dis + 1

                    if (newr, newc) == destination:
                        return dis + 1
                    
                    q.append((dis + 1, (newr, newc)))

        return -1

if __name__ == "__main__":
    source = (0, 1)
    destination = (2, 2)

    grid = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1]
    ]

    obj = Solution()
    res = obj.shortestPath(grid, source, destination)

    print(res)
