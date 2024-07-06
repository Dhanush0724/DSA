
def searchinsert(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    ans = n
    while low<=high:
        mid = (low+high)//2

        if arr[mid] >= target:
            ans = mid
            high = mid-1
        else :
            low = mid+1
    return ans



        
    
if __name__ == "__main__":
    arr = [1,2,4,7]
    
    target = 6
    ind = searchinsert(arr, target)
    print("The insert is the index:", ind)
    