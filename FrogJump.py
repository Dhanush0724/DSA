# ###########   RECURSION
# def f(n,height):
#     if(n==0):
#         return 0
#     one = f(n-1,height)+abs(height[n]-height[n-1])
#     two = float('inf')
#     if n>1:
#         two = f(n-2,height) + abs(height[n]-height[n-2])
    
#     return min(one,two)

# height = [30, 10, 60, 10, 60, 50]
# n = len(height)-1

# print(f(n, height))

# ###############         MEMORIZATION
# import sys,math
# def f(i,height,dp):
#     if i == 0:
#         return 0
#     if dp[i]!=-1:
#         return dp[i]
#     jumptwo = sys.maxsize
#     jumpone = f(i-1,height,dp) + abs(height[i] - height[i-1])
#     if i > 1:
#         jumptwo = f(i-2,height,dp) + abs(height[i] -height[i-2])
#     dp[i] = min(jumpone,jumptwo)
#     return dp[i]

# height = [30, 10, 60, 10, 60, 50]
# n = len(height)
# dp = [-1] * n
# print(f(n-1, height, dp))


############## TABULATION

# height = [30,10,60,10,60,50]
# n = len(height)
# dp = [-1 for _ in range(n)]
# dp[0] = 0
# for i in range(1,n):
#     jumptwo = float('inf')
#     jumpone = dp[i-1] + abs(height[i] - height[i-1])
#     if i > 1:
#         jumptwo = dp[i-2] + abs(height[i]- height[i-2])
#     dp[i] = min(jumpone,jumptwo)
# print(dp[n-1])

############## SPACE OPTIMIZATION 
import sys
height  = [30,10,60,10,60,50]
n = len(height)
prev = 0
prev2  = 0
for i in range(1,n):
    jumptwo = sys.maxsize
    jumpone = prev  + abs(height[i] - height[i-1])
    if i>1:
        jumptwo = prev2 + abs(height[i]- height[i-2])
    cur = min(jumpone,jumptwo)
    prev2 = prev
    prev = cur
print(prev)