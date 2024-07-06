
def upperBound(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    ans = n
    while low<=high:
        mid = (low+high)//2

        if arr[mid] > target:
            ans = mid
            
            high = mid-1
            
        else :
            low = mid+1
    return ans
if __name__ == "__main__":
    arr = [3, 5, 8, 9, 15, 19]
    
    target = 9
    ind = upperBound(arr, target)
    print("The upper bound is the index:", ind)
    