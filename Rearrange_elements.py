

def rearange(arr):
    n = len(arr)


    ans = [0] *n
    posIndex, negIndex = 0,1
    for i in range(n):

        if arr[i] < 0:
            ans[negIndex] = arr[i]
            negIndex +=2
        else :
            ans[posIndex] = arr[i]
            posIndex +=2
    return ans
     

   
arr = [1,2,-4,-5,3,4]
print(rearange(arr))
