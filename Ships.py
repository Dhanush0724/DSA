
def finddays(weights,cap):
    day = 1
    load = 0
    n = len(weights)

    for i in range(n):

        if load+weights[i] > cap:
            day +=1
            load = weights[i]
        else :
            load += weights[i]
    return day

def leastweigthcapacity(weights,d):

    low = max(weights)
    high = sum(weights)

    while low<=high:

        mid = (low+high)//2

        numberofdays = finddays(weights,mid)

        if numberofdays <= d:
            high = mid-1
        else :
            low = mid+1
    return low



weights  = [5,4,5,2,3,4,5,6]
d = 5
print(leastweigthcapacity(weights,d))