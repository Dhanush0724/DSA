###########################    RECURSION
# def f(i, j, maze):
   
#     if i < 0 or j < 0:
#         return 0

#     if maze[i][j] == -1:
#         return 0

#     if i == 0 and j == 0:
#         return 1
  
#     up = f(i-1, j, maze)
#     left = f(i, j-1, maze)
    
#     return up + left

# maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
# n = len(maze)  
# m = len(maze[0])  

# result = f(n-1, m-1, maze)
# print(result)

###########################   MEMORIZATION

# def f(i,j,maze,dp):

#     if i<0 or j<0 or maze[i][j] == -1:
#         return 0
#     if i == 0 and j == 0:
#         return 1
    
#     if dp[i][j] != -1:
#         return dp[i][j]
    
#     up = f(i-1,j,maze,dp)
#     left = f(i,j-1,maze,dp)

#     dp[i][j] = up+left
#     return dp[i][j]

# maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
# n = len(maze)  
# m = len(maze[0])  
# dp = [[-1 for j in range(m)] for i in range(n)]
# result = f(n-1, m-1, maze,dp)
# print(result)

#########  TABULATION

def f(n,m,maze,dp):

    for i in range(n):
        for j in range(m):

            if maze[i][j] == -1:
                dp[i][j] = 0
                continue
                

            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            up =  0
            left  = 0

            if i > 0:
                up = dp[i-1][j]

            if j > 0:
                left = dp[i][j-1]

            dp[i][j] = up+left

    return dp[n-1][m-1]           


maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
n = len(maze)  
m = len(maze[0])  
dp = [[-1 for j in range(m)] for i in range(n)]
result = f(n, m, maze,dp)
print(result)