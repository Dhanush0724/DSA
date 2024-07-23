class solutiuon:

    def subsetsum(self,arr,n):
        ans = []

        def subsetsumhelp(i,sum):
            if i == n:
                ans.append(sum)
                return 
            
            subsetsumhelp(i+1,sum)

            subsetsumhelp(i+1,sum+arr[i])
        subsetsumhelp(0,0)
        ans.sort()
        return ans
    
arr = [3,1,2]
res = solutiuon().subsetsum(arr,len(arr))
print(" ".join(map(str,res)))