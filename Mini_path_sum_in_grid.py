#########################   RECURSION
# def f(i,j,matrix):

#     if i==0 and j == 0:
#         return matrix[i][j] 
#     if i <0 or j<0:
#         return int(1e9)
#     up = matrix[i][j] + f(i-1,j,matrix)
#     left = matrix[i][j] + f(i,j-1,matrix)

#     return min(up,left)

# matrix = [[5, 9, 6],
#               [11, 5, 2]]
# n = len(matrix)
# m = len(matrix[0])
# print(f(n-1, m-1, matrix))

############################  MEMORIZATION

# def f(i,j,matrix,dp):
    
#     if i==0 and j == 0:
#         return matrix[0][0]
    
#     if i<0 or j<0:
#         return int(1e9)
    
#     if dp[i][j] != -1:

#         return dp[i][j]

#     up = matrix[i][j] + f(i-1,j,matrix,dp)
#     left = matrix[i][j] + f(i,j-1,matrix,dp)

#     dp[i][j] = min(up,left)
    
    
#     return dp[i][j]
    
# matrix = [[5, 9, 6],
#                [11, 5, 2]]
# n = len(matrix)
# m = len(matrix[0])
# dp = [[-1 for j in range(m)] for i in range(n)]
# print(f(n-1, m-1, matrix,dp))
# .


##################   TABULATION

def f(n,m,matrix,dp):

    for i in range(n):
        for j in range(m):

            if i==0 and  j == 0:
                dp[i][j] = matrix[i][j]
            
            else :
                up = dp[i-1][j] if i>0 else int(1e9)

                left = dp[i][j-1] if j>0 else int(1e9)

                dp[i][j] = min(up,left) + matrix[i][j]
    
    return dp[n-1][m-1]





matrix = [[5, 9, 6],
               [11, 5, 2]]
n = len(matrix)
m = len(matrix[0])
dp = [[-1 for _ in range(m)] for _ in range(n)]
print(f(n, m, matrix,dp))

