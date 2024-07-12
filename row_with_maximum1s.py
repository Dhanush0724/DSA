# Input Format:
#  n = 3, m = 3, 
# mat[] = 
# 1 1 1
# 0 0 1
# 0 0 0
# Result:
#  0
# Explanation:
#  The row with the maximum number of ones is 0 (0 - indexed).

###### Brute Force approach

# def rowwithmax(matrix,n,m):
#     cnt_max = 0
#     index = -1

#     for i in range(m):
#         cnt_ones = sum(matrix[i])
#         if cnt_ones > cnt_max:
#             cnt_max = cnt_ones
#             index = i
#     return index

# matrix = [[1,1,1],[0,0,1],[0,0,0]]
# n = 3
# m = 3
# print(rowwithmax(matrix,n,m))


# OPtimal approach bs

def lowerbound(arr,n,x):
    low = 0
    high = n-1
    ans = n

    while low<=high:
        mid = (low+high)//2

        if arr[mid] >=x:
            ans = mid
            high = mid-1
        else :
            low = mid+1
    return ans

def rowwithmax(matrix,n,m):
    cnt_max = 0
    index = -1
    for i in range(n):

        count_ones =  m - lowerbound(matrix[i],m,1)
        if count_ones > cnt_max:
            cnt_max = count_ones
    return index

matrix = [[1,1,1],[0,0,1],[0,0,0]]
n = 3
m = 3
print(rowwithmax(matrix,n,m))