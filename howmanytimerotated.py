import sys
def minimum_in_rotated(arr):
    n = len(arr)
    low = 0
    high = n-1
    index = -1
    ans = sys.maxsize
    while low<=high:

        mid = (low+high)//2
        ### high is deiifrent 
        #search space is already sorted
        # then arr[low] will always be
        # the minimum in that search space:
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                index = low
            break
            
        if arr[low]<=arr[mid]:
            if arr[low] < ans:
                index = low
            low = mid+1
        else :
             if arr[mid ] < ans:
                 index = mid
                 ans = arr[mid]
             high = mid-1
               
    return index 

arr = [4,5,6,7,1,2,3]
print(minimum_in_rotated(arr))