from timedecor import time_it

@time_it
def BinarySearch(arr,x):

    low = 0
    high = len(arr) -1
    mid = 0

    while low<=high:

        mid = (low+high)//2

        if arr[mid] > x:
            high = mid-1

        elif arr[mid] < x:
            low = mid+1

        else :
            return mid
        
    return -1

arr = [i for i in range(10000000)]
x = 90000


print("element found at ",BinarySearch(arr,x))
    
