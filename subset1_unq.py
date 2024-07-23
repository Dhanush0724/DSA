class solution:

    def subset(self,nums):
        ans = []
        ds = []

        def findsubset(ind):
            ans.append(ds[:])
            for i in range(ind,len(nums)):
                if i != ind and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                findsubset(i+1)
                ds.pop()
        nums.sort()
        findsubset(0)
        return ans
    
nums = [1,2,2]
res = solution().subset(nums)
print(' '.join(map(str,res)))