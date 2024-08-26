#####################   RECURSION
# def countWays(i,j):

#     if i == 0 and j == 0:
#         return 1
#     if i<0 or j<0:
#         return 0
#     up = countWays(i-1,j)
#     left = countWays(i,j-1)

#     return up+left

# m = 3
# n = 2
# print(countWays(m-1, n-1))

############################  MEMORIZATION

# def countWays(i,j,dp):

#     if i== 0 and j == 0:
#         return 1
#     if i<0 or j<0:
#         return 0
    
#     if dp[i][j] != -1:
#         return dp[i][j]
#     up = countWays(i-1,j,dp)
#     left = countWays(i,j-1,dp)
    
#     dp[i][j] = up + left
#     return dp[i][j]
    


# m = 3
# n = 2
# dp = [[-1 for j in range(n)]for i in range(m)]
# print(countWays(m-1, n-1,dp))

#################   TABULATION

def countWays(m,n,dp):

    for i in range(m):
        for j in range(n):
            if i == 0  and j == 0:
                dp[i][j] = 1
                continue
            up = 0
            left = 0

            if i > 0:
                up = dp[i-1][j]
            
            if j > 0 :
                left = dp[i][j-1]
            
            dp[i][j] = up + left
    
    return dp[m-1][n-1]



m = 3
n = 2
dp = [[-1 for j in range(n)]for i in range(m)]
print(countWays(m, n,dp))