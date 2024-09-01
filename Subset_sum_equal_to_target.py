
# ########################  RECURSION
# def f(i,k,arr):
#     if k== 0:
#         return True
#     if i == 0:
#         return arr[0] == k
    
#     nottake = f(i-1,k,arr)
#     take = False

#     if k>arr[i]:
#         take = f(i-1,k-arr[i],arr)
    
#     return nottake or take

# def subsetSumToK(n,k,arr):

#     return f(n-1,k,arr)

# arr = [1, 2, 3, 4]
# k = 4
# n = len(arr)

# if subsetSumToK(n, k, arr):
#     print("Subset with the given target found")
# else:
#     print("Subset with the given target not found")



##################################   MEMORIZATION

# def f(i,target,arr,dp):

#     if target == 0:
#         return True
    
#     if i == 0:
#         return arr[0] == target

#     if dp[i][target] != -1:
#         return dp[i][target]

#     nottaken = f(i-1,target,arr,dp)

#     taken = False

#     if arr[i] <= target:
#         taken = f(i-1,target-arr[i],arr,dp)

#     dp[i][target] = nottaken or taken
#     return dp[i][target]    

# def subsetSumToK(n,k,arr):

#     dp = [[-1 for j in range(k+1)] for i in range(n)]
#     return f(n-1,k,arr,dp)

# arr = [1, 2, 3, 4]
# k = 4
# n = len(arr)

# if subsetSumToK(n, k, arr):
#     print("Subset with the given target found")
# else:
#     print("Subset with the given target not found")


############################  TABULATION

def f(n,k,arr,dp):

    for i in range(n):
        dp[i][0] = True
    
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    for i in range(1,n):
        for target in range(1,k+1):
            nottaken = dp[i-1][target]
            taken = False

            if arr[i] <= target:
                taken = dp[i-1][target-arr[i]]
            dp[i][target] = nottaken or taken
        
    return dp[n-1][k]




def subsetSumToK(n,k,arr):

    dp = [[True for j in range(k+1)] for i in range(n)]
    return f(n,k,arr,dp)

arr = [1, 2, 3, 4]
k = 4
n = len(arr)

if subsetSumToK(n, k, arr):
    print("Subset with the given target found")
else:
    print("Subset with the given target not found")