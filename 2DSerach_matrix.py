# Input Format:
#  N = 3, M = 4, target = 8,
# mat[] = 
# 1 2 3 4
# 5 6 7 8 
# 9 10 11 12
# Result:
#  true
# Explanation:
#  The ‘target’  = 8 exists in the 'mat' at index (1, 3).


##Brute Force Method:::::::::

# def serach2d(arr,n,m,target):

#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == target:
#                 return (i,j)

# arr= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# n = 4
# m = 4
# target = 8
# print(serach2d(arr,n,m,target))


###### OPTIMAL SOLUTION...............

def serachmatrix(matrix,target):
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = n*m-1

    while low<=high:
        mid = (low+high)//2
        row = mid//m
        col = mid%m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid+1
        else :
            high = mid -1
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = serachmatrix(matrix, 8)
print("true" if result else "false")

