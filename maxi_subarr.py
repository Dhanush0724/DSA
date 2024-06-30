# #### my APProach .........
# import sys
# def max_sub_arr(arr):
#     n = len(arr)
#     maxi = -sys.maxsize 
#     print(maxi)
    
#     for i in range(n):
#         for j in range(i,n):
#             sum = 0
            
#             for k in range(i,j+1):
#                 sum += arr[k]

#             maxi = max(maxi,sum)
#     return maxi

# arr  = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_sub_arr(arr))

import sys
def max_subarray(arr):
    maxi = -sys.maxsize -1
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]

        if sum > maxi:
              maxi = sum

        if sum < 0:
             sum = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxSum = max_subarray(arr)
print("The maximum subarray sum is:", maxSum)
