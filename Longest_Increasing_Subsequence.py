#####  recursion
# def longest_increasing_subsequence_length(ind, prev_index,arr):

#     n = len(arr)
#     if ind == n:
#         return 0
    
#     nottake = 0 + longest_increasing_subsequence_length(ind+1,prev_index,arr)
#     take = 0
#     if prev_index == -1 or arr[ind] > arr[prev_index]:
        
#         take = 1+longest_increasing_subsequence_length(ind+1,ind,arr)
    
#     return max(nottake,take)


# if __name__ == "__main__":
#     arr = [10, 9, 2, 5, 3, 7, 101, 18]
#     prev = -1
#     result = longest_increasing_subsequence_length(0,prev,arr)
#     print("The length of the longest increasing subsequence is", result)


####### MEMORIZATION

def longest_increasing_subsequence_length(arr,n,ind, prev_index,dp):

    
    if ind == n:
        return 0
    
    if dp[ind][prev_index+1] !=-1:
        return dp[ind][prev_index+1]
    

    nottake = 0 + longest_increasing_subsequence_length(arr,n,ind+1,prev_index,dp)
    take = 0
    if prev_index == -1 or arr[ind] > arr[prev_index]:
        
        take = 1+longest_increasing_subsequence_length(arr,n,ind+1,ind,dp)
    
    dp[ind][prev_index+1] = max(nottake,take)
    return dp[ind][prev_index+1]


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]

    n = len(arr)
    dp = [[-1 for _ in range(n+1)] for _ in range(n)]
    result = longest_increasing_subsequence_length(arr,n,0,-1,dp)
    print("The length of the longest increasing subsequence is", result)