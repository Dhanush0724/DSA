


def binary(arr,target):
    n = len(arr)
    low = 0
    high =  n-1

    while low<=high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid+1
        else :
            high = mid-1
    return -1


arr  = [3,4,5,6,7,9,12,16,17]
target = 6
res = binary(arr,target)
if res == -1:
    print("target is not present")
else :
    print("The target is at index:", res)