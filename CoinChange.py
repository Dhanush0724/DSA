# ####################   MEMORIZATION
# def f(arr,i, t, dp):

#     if i == 0:
#         return 1 if t%arr[0] == 0 else 0
    
#     if dp[i][t] != -1:
#         return dp[i][t]
    
#     nottaken = f(arr,i-1,t,dp)
#     taken = 0

#     if arr[i] <= t:
#         taken = f(arr,i,t-arr[i],dp)
    
#     dp[i][t] = nottaken+taken
#     return dp[i][t]

# def countWaysToMakeChange(arr,n,t):
#     dp = [[-1 for i in range(t+1)] for j in range(n)]
#     return f(arr,n-1,t,dp) 

# arr = [1, 2, 3]
# target = 4
# n = len(arr)
# print("The total number of ways is", countWaysToMakeChange(arr, n, target))


##### #####  TABULATION


def f(arr,n, t, dp):
  
  for i in range(t+1):
    if i%arr[0] == 0:
      dp[0][i] = 1
    
    
  for i in range(1,n):
    for target in range(t+1):
      
      nottaken = dp[i-1][target]
      taken = 0
      if arr[i] <= target:
        taken = dp[i][target-arr[i]]

      dp[i][target] =   nottaken + taken

  return dp[n-1][t]


def countWaysToMakeChange(arr,n,t):
   dp = [[-1 for _ in range(t+1)] for _ in range(n)]
   return f(arr,n,t,dp) 

arr = [1, 2, 3]
target = 4
n = len(arr)
print("The total number of ways is", countWaysToMakeChange(arr, n, target))
