
def maxCoins(a):
    n = len(a)

    a.insert(0,1)
    a.append(1)

    dp = [[-1]*(n+2) for _ in range(n+2)]

    def f(i,j):
        if i >j:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        maxi = float('-inf')
        for ind in range(i,j+1):
            cost = a[i-1]*a[ind]*a[j+1]+f(i,ind-1)+f(ind+1,j)
            maxi = max(maxi,cost)
        dp[i][j] = maxi
        return maxi
    
    return f(1,n)

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    ans = maxCoins(a)
    print(ans)



##################   TBAULATIONI

def maxCoins(a):
    n = len(a)

    a.insert(0,1)
    a.append(1)

    dp = [[-1]*(n+2) for _ in range(n+2)]

    for i in range(n,0,-1):
        for j in range(1,n+1):
            if i>j:
                continue
            maxi = float('-inf')

            for ind in range(i,j+1):
                cost = a[i-1]*a[ind]*a[j+1] +dp[i][ind-1] + dp[ind+1][j]
                maxi = max(maxi,cost)

            dp[i][j] = maxi
    return dp[1][n]

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    ans = maxCoins(a)
    print(ans)