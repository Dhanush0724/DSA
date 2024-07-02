
def printleaders(arr,n):
    ans = []

    for i in range(n):
        leader = True

        for j in range(i+1,n):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            ans.append(arr[i])
    return ans

arr = [10,22,12,3,0,6]
n= 6
print(printleaders(arr,n))