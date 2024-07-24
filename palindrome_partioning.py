class plaindrome:

    def partition(self,s):
        res = []
        path = []

        def partitionmaker(index):

            if index == len(s):
                res.append(path[:])
                return
            for i in range(index,len(s)):
                if ispalindrome(s,index,i):
                    path.append(s[index:i+1])
                    partitionmaker(i+1)
                    path.pop()

        def ispalindrome(s,start,end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start+=1
                end-=1
            return True
        
        partitionmaker(0)
        return res


if __name__ == "__main__":
    s = "aabb"
    obj = plaindrome()
    ans = obj.partition(s)
    print(' '.join(map(str,ans)))
    
