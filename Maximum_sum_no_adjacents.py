###########  RECURSION
# def f(n,arr):
#     if n==0:
#         return arr[n]
    
#     if n<0:
#         return 0
    
#     pick = arr[n] + f(n-2,arr)
#     nopick = 0 + f(n-1,arr)

#     return max(pick,nopick)

# arr = [2, 1, 4, 9]
# n = len(arr)-1
# print(f(n, arr))

###################  MEMORIZATION

# def f(n,arr,dp):

#     if n == 0:
#         return arr[n]
#     if n<0 :
#         return 0
    
#     if dp[n]!=-1:
#         return dp[n]
    
#     pick = arr[n] + f(n-2,arr,dp)
#     nopick = 0 + f(n-1,arr,dp)
#     dp[n] = max(pick,nopick)
#     return dp[n]

# arr = [2,1,4,9]
# n = len(arr) - 1
# dp = [-1]*(len(arr))
# print(f(n,arr,dp))

########################  TABULATION 

# def f(n,arr,dp):

#     if n == 0:
#         return arr[n]
#     if n<0 :
#         return 0
    
#     dp[0] = arr[0]

#     if n>0:
#         dp[1] = max(arr[0],arr[1])

#     for i in range(2,n+1):
#         pick = arr[i] + dp[i-2]
#         nopick = dp[i-1]
#         dp[i] = max(pick,nopick)

#     return dp[n]    
    
# arr = [2,1,4,9]
# n = len(arr) - 1
# dp = [-1]*(len(arr))
# print(f(n,arr,dp))

# ######################   SPACE OPTIMISATION

def f(n,arr,dp):

    if n == 0:
        return arr[n]
    if n<0 :
        return 0
    
    prev = arr[0]

    if n>0:
        prev2 = max(arr[0],arr[1])

    for i in range(2,n+1):
        pick = arr[i] + prev2
        nopick = prev
        curr = max(pick,nopick)
        prev2 = prev
        prev = curr


    return prev   
    
arr = [2,1,4,9]
n = len(arr) - 1
dp = [-1]*(len(arr))
print(f(n,arr,dp))
