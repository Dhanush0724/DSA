
def f(i,target,arr,dp):

    if i == 0:

        if target == 0 and arr[0] == 0:
            return 2
        if target == 0 or target == arr[0]:
            return 1
        return 0
    
    if dp[i][target]!=-1:
        return dp[i][target]
    
    nottaken = f(i-1,target,arr,dp)

    taken = 0
    if arr[i] <= target:
        taken = f(i-1,target-arr[i],arr,dp)
    
    dp[i][target] = nottaken+taken
    return dp[i][target]




def targetSum(n, target, arr):
    totalsum = 0
    for i in range(len(arr)):
        totalsum+=arr[i]

    if totalsum-target<0:
        return 0 
    if (totalsum-target)%2==1:
        return 0
    
    s2 = (totalsum-target)//2

    dp = [[-1 for j in range(s2+1)] for i in range(len(arr))]

    return f(n-1,s2,arr,dp)


arr = [1, 2, 3, 1]
target = 3
n = len(arr)
print("The number of ways found is", targetSum(n, target, arr))