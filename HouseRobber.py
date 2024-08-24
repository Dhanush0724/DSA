def f(arr):
    n = len(arr)
    prev = arr[0]
    prev2 = 0

    for i in range(1,n):
        pick = arr[i]
        if i> 1:
            pick+=prev2
        nopick = 0 + prev

        curr = max(pick,nopick)
        prev2 = prev
        prev = curr
    
    return prev

def robstreet(n,arr):
    arr1 = []
    arr2 = []

    if n==1:
        return arr[0]
    
    for i in range(n):
        if i != 0:
            arr1.append(arr[i])
        if i !=n-1:
            arr2.append(arr[i])
    
    ans1 = f(arr1)
    ans2 = f(arr2)

    return max(ans1,ans2)

arr = [1,5,1,2,6]
n = len(arr)
print(robstreet(n,arr))
