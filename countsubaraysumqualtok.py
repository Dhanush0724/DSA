#Count Subarray sum Equals K
def subarray(arr,n,k):
    count = 0
    for i in range(n):
        current_sum = 0
        for j in range(i,n):    
            current_sum +=arr[j]
            #subarray = sum(arr[i:j+1])
            if current_sum == k:
                count+=1
    return count
if __name__ == "__main__":
    arr = [3,1,2,4]
    k = 6
    n= 4
    print(subarray(arr,n,k))