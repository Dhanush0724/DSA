# ## Largest Element in aN Array
# arr = [5,6,7,8,2,3,3,9]
# max = 0
# for i in range(len(arr)):
#     if max<arr[i]:
#         max = arr[i]
# sorted = arr.sort()
# print(arr[-1])
# print(max)

# ## second largest element in an array wihtout sorting it
# def second_largest(arr):
#     if len(arr) < 2:
#         return None
#     max1 = 0
#     max2 = 0
#     for num in arr:
#         if num >max1:
#             max2 = max1
#             max1 = num
#         elif num>max2 and num != max1:
#             max2 = num
#     return max2
# if __name__ == "__main__":
#     arr = [5,6,8,3,1,9,2,4]
#     res= second_largest(arr)
#     print(res)

# check if the array is sorted
# def array_is_sorted(arr):
#     for i in range(1,len(arr)):
#         if arr[i] < arr[i-1]:
#             return False
#     return True
# test_cases = [
#     [5, 1, 2, 3, 4],
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 5, 4],
#     [2, 2, 2, 2, 2],
#     [1],
#     [2, 1]
# ]
# for i,test_case in enumerate(test_cases, start = 1):
#     res = array_is_sorted(test_case)
#     if res :
#         print(f"Test case {i} is sorted :YES")
#     else :
#         print(f"Test case {i} is sorted :NO")



######### Remove duplicates from sorted array

# arr = [2,3,5,4,5,6,3,6]
# arr.sort()
# un = []
# for num in arr:
#     if num not in un:
#         un.append(num)
# print(un)

##Left rotate array by one

# def LeftRotate(arr,n):
#     temp = arr[0]
#     for i in range(n-1):
#         arr[i] = arr[i+1]
#     arr[n-1] = temp

#     for i in range(n):
#         print(arr[i],end="")
# n = 5
# arr = [1,2,3,4,5]
# LeftRotate(arr,n)

# Rotate array by k elements

# def Rotate(arr,n,k):

#     #just put in the case k = k%n
#     return arr[-k:] + arr[:-k]

# n = 7
# arr  = [1,2,3,4,5,6,7]
# k=2
# print(Rotate(arr,n,k))

## Move zeros to end of the array

# def MoveZer(arr,n):

#     j = -1

#     for i in range(n):
#         if arr[i] == 0:
#             j = i
#             break
#     if j == -1:
#         return arr
    
#     for i in range(j+1,n):
#         if arr[i] !=0:
#             arr[i],arr[j] = arr[j],arr[i]
#             j +=1
#     return arr

# arr = [1,0,2,3,2,0,0,4,5]
# n = 9
# res = MoveZer(arr,n)
# for i in res:
#     print(i,end="")
# print()
            
# array union

# def union_array(arr1,arr2):
#     i,j = 0,0
#     union_result = []

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             if not union_result or union_result[-1] != arr1[i]:
#                 union_result.append(arr1[i])
#             i +=1
#         elif arr1[i] > arr2[j]:
#             if not union_result or union_result[-1]!= arr2[j]:
#                 union_result.append(arr2[j])
#             j+=1
#         else :
#             if not union_result or union_result[-1] != arr1[i]:
#                  union_result.append(arr1[i])
#             i +=1
#             j +=1
        
#     while i < len(arr1):
#         if not union_result or union_result[-1]!= arr1[i]:
#             union_result.append(arr1[i])
#         i+=1
#     while j < len(arr2):
#         if not union_result or union_result[-1]!= arr2[j]:
#             union_result.append(arr2[j])
#         j+=1

#     return union_result
# n = 5
# m = 5
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 3, 4, 4, 5]
# result = union_array(arr1, arr2)
# print(result)


# missing number in arraY

# def missing(arr,n):

#     summation = (n*(n+1)) // 2
   
    
#     s2 = sum(arr)
    
#     missingnum = summation - s2
#     return missingnum
# arr = [1,2,4,5]
# n = 5

# print(missing(arr,n))

###consective one's in the array

# def ones(arr):
#     count = 0
#     maxi = 0
#     for i in range(len(arr)):
#         if arr[i] == 1:
#             count+=1
#         else : 
#             count = 0
#         maxi = max(maxi,count)
#     return maxi

# arr = [1,1,0,1,1,1]
# print(ones(arr))

# find numbers which appers onces
 
# def apperones(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         num = arr[i]
#         for j in range(n):
#             if arr[j] == num:
#                 count+=1
#         if count == 1:
#             return num
#     return -1

# def apperoptimal(arr):
#     xorr  =0
#     for num in arr:
#         xorr ^= num
#     return xorr

# arr = [4,1,2,1,2]
# print(apperones(arr))
# print(apperoptimal(arr))

### longest subarrray with givenm sum k

def longestsubarray(arr,n,k):
    
    left,right = 0,0
    sum = 0
    maxlen = 0

    while right<n:

        sum += arr[right]

        while sum > k and left<=right:
            sum -=arr[left]
            left += 1

        if sum == k:
            maxlen = max(maxlen,right-left+1) 

        right += 1
        
    return maxlen

    

arr = [2, 3, 5, 1, 9]
n = 3
k =5
print(longestsubarray(arr,n,k))












        




    

