##  Brute Force O(n2)
# def MaxConsecutiveOnes(nums,k):
#     n = len(nums)
#     maxlen = 0
#     for i in range(n):
#         zeros = 0
#         for j in range(i,n):
#             if (nums[j]==0):
#                 zeros+=1
#             if (zeros<=k):
#                 length = j-i+1
#                 maxlen = max(maxlen,length)
#             else :
#                 break  
#     return maxlen



#Optimal sliding window
# def MaxConsecutiveOnes(nums,k):
#     maxlen = 0
#     l = 0
#     r = 0
#     n = len(nums)
#     zeros = 0
#     while (r<n):
#         if nums[r] == 0:
#             zeros+=1
#         while (zeros>k):
#             if nums[l] == 0:
#                 zeros-=1
#             l+=1
       
#         length = r-l+1
#         maxlen = max(maxlen,length)
#         r+=1
#     return maxlen



### More more Optimal

def MaxConsecutiveOnes(nums,k):
    left = 0
    right = 0
    zeros = 0
    maxlen = 0
    n= len(nums)
    while right < n:
        if nums[right] == 0:
            zeros+=1
        if zeros>k:
            if nums[left] == 0:
                zeros-=1
            left+=1
       
            length = right-left+1
            maxlen = max(maxlen,length)
        right+=1
    return maxlen


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(MaxConsecutiveOnes(nums,k))




 