

def jump(nums):

    maxi = 0
    n = len(nums)
    for i in range(n):
        if i > maxi :
            return False
        maxi = max(maxi,i+nums[i])

    return True

nums = [3,2,1,0,4]
print(jump(nums))