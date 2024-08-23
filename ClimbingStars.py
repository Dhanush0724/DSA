### Tabulation method

def main():

    n = 3
    dp = [-1]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[n])

main()


#### OPTIMISE 

def main():
    n = 3
    prev2 = 1
    prev = 1

    for i in range(2,n+1):
        curi = prev2+prev
        prev2 = prev
        prev = curi
    
    print(prev)
main()