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




    

