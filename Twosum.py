
# my appraoch is dynamic approach complexity is O(n^2) nested loop
def two_sum(arr,n,target):

    # #my approach
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if arr[i] + arr[j] == target:
    #             return True
    # return False

    prevmap = {}

    for i,num in enumerate(arr):
        diff = target - num
        print(diff)
        if diff in prevmap:
            return [prevmap[diff],i]
        prevmap[num] = i
    return -1
arr = [2,6,5,8,11]
n = 5
target = 15
res = two_sum(arr,n,target)

if res != -1 :
    print("YES",res)
else :
    print("NO")


