
def partition(arr,low,high):
    pivot = arr[low]
    i = low+1
    j = high


    while i<=j:
        while i<=j and arr[i] <= pivot:
            i = i+1
        while i<=j and arr[j] >=pivot:
            j = j-1
        
        if i <j:
            arr[i],arr[j]  = arr[j],arr[i]
        else :
            break

    arr[low],arr[j] = arr[j],arr[low]
    return j

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

test_cases = [
    [8, 7, 2, 1, 0, 9, 6],
    [1, 2, 3, 4, 5, 6, 7],
    [],
    [1],
    [3, 2, 1, 12, 3, 2, 3]
]

for data in test_cases:
    print("Unsorted array:")
    print(data)

    quicksort(data, 0, len(data) - 1)
    print("Sorted array in ascending order:")
    print(data)
    print()