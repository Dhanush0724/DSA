# Input: N = 11, A[] = {3,10,4,2,1,2,6,1,7,2,9}

# Output: 10,-1,6,6,2,6,7,7,9,9,

###### Brute force Method
# N = 11
# A = [3,10,4,2,1,2,6,1,7,2,9]
# nge = []
# for i in range(N):
#     found = False
#     for j in range(i+1,N):
#         if A[j] > A[i]:
#             nge.append(A[j])
#             found = True
#             break
#     if not found:
#         for j in range(0,i):
#             if A[j] > A[i]:
#                 nge.append(A[j])
#                 found = True
#                 break
#     if not found :
#         nge.append(-1)     
# print(nge)


#### Optimal Approach............


class Solution:

    def nextgreaterelements(self,nums):
        n = len(nums)
        nge = [-1]*n
        st = []

        for i in range(2*n-1,-1,-1):
            while st and st[-1] >= nums[i%n]:
                st.pop()
            
            if i <n:
                if st:
                    nge[i] = st[-1]
            st.append(nums[i%n])
        return nge
obj = Solution()
v = [3,2,1]
res = obj.nextgreaterelements(v)
print("The next greater elements are")
print(*res)



