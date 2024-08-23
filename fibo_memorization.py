
def f(n,dp):

    if n <= 1:
        return n
    
    if dp[n] !=-1:
        return dp[n]
    dp[n] = f(n-1,dp)+f(n-1,dp)
    return dp[n]

if __name__ == "__main__":
    n = 5
    dp = [-1]*(n+1)
    print(f(n,dp))