

def jump(nums):

    maxi = 0
    n = len(nums)
    jumps = 0
    current_end  = 0
    for i in range(n-1):

        maxi = max(maxi,i+nums[i])

        if i == current_end:
            jumps+=1
            current_end = maxi

            if current_end >= n-1:
                break
    return jumps



        

    

nums = [3,2,1,0,4]
print(jump(nums))