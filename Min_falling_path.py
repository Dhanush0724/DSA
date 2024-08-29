# #########################  RECURSION

# def f(i,j,matrix):

#     if j<0 or j>=len(matrix[0]):
#         return int(-1e9)
    
#     if i== 0 :
#         return matrix[0][j]
    
#     st = matrix[i][j] + f(i-1,j,matrix)
#     leftup = matrix[i][j] + f(i-1,j-1,matrix)
#     rightup = matrix[i][j] + f(i-1,j+1,matrix)

#     return max(st,leftup,rightup)


# matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
# n = len(matrix)
# m = len(matrix[0])
# result = max(f(n-1, j, matrix) for j in range(m))
# print(result)

####################  MEMORIZATION
# def f(i,j,matrix,dp):

#     if j<0 or j>=len(matrix[0]):
#         return -int(1e9)
#     if i== 0:
#         return matrix[0][j]

#     if dp[i][j] != -1:
#         return matrix[0][j]
    
#     up = matrix[i][j] + f(i-1,j,matrix,dp)
#     leftdiagonal = matrix[i][j] + f(i-1,j-1,matrix,dp)
#     rightdiagonal = matrix[i][j] + f(i-1,j+1,matrix,dp)

#     dp[i][j] = max(up,leftdiagonal,rightdiagonal)

#     return dp[i][j]

# matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
# n = len(matrix)
# m = len(matrix[0])
# dp = [[-1 for _ in range(m)] for _ in range(n)]
# result = max(f(n-1, j, matrix,dp) for j in range(m))
# print(result)

###################   TABULATION

def f(matrix,dp):

    for j in range(m):
        dp[0][j] = matrix[0][j]
    
    for i in range(1,n):
        for j in range(m):

            up = matrix[i][j] + dp[i-1][j]

            leftdiagonal = matrix[i][j] + dp[i-1][j-1] if j-1>=0 else -int(1e9)

            rightdiagonal = matrix[i][j] + dp[i-1][j+1] if j+1<m else -int(1e9)

            dp[i][j] = max(up,leftdiagonal,rightdiagonal)

    return max(dp[n-1][j] for j in range(m))


matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
n = len(matrix)
m = len(matrix[0])
dp = [[-1 for _ in range(m)] for _ in range(n)]
result = f(matrix,dp)
print(result)