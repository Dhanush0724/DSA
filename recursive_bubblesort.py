
def bubblesort(arr,n=None):
    if n is None:
        n = len(arr)
    if n  == 1:
         return
    for i in range(n-1):
         if arr[i] > arr[i+1]:
              arr[i],arr[i+1] = arr[i+1],arr[i]

    bubblesort(arr,n-1)
arr = [3,6,5,4,8,9,2,1]
bubblesort(arr)
print(arr)