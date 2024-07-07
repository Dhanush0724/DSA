

def first(arr,x):
    n = len(arr)
    first = 0
    last = 0
    low = 0
    high = n-1

    while low<=high:
        mid  = (low+high)//2

        if arr[mid] == x:
            first = mid
            high = mid-1
        
        if arr[mid] <x:
            low = mid+1
        high = mid-1
    return first

def last(arr,x):
    n = len(arr)
    first = 0
    last = 0
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2

        if arr[mid] == x:
            last = mid
            low = mid+1
        
        elif arr[mid]< x:
            low = mid+1
        else :
            high = mid-1

    return last

def firstlast(arr,x):
    fir = first(arr,x)
    if fir == -1:
        return(-1,-1)
    la = last(arr,x)
    return (fir,la)

def count(arr,x):
    first,last = firstlast(arr,x)
    if first ==-1:
        return 0
    return last - first +1

arr = [2,4,6,8,8,8,11,13]
x= 8
print(count(arr,x))