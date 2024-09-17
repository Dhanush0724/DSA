###############   BRUTE FORCE only one stock
stocks = [7,1,5,3,6,4]
mini = stocks[0]
profit = 0
for i in range(1,len(stocks)):
    price = stocks[i] - mini
    profit = max(profit,price)
    mini = min(mini,stocks[i])
print(profit)


##################   RECURSION  any number of stocks

def getMaximumProfit(Arr,n):

    if n==0:
        return 0
    
    def getAns(ind,buy):

        if ind == n:
            return 0
        
        profit = 0 
        if  buy == 0:
            profit = max(0+getAns(ind+1,0),-Arr[ind]+getAns(ind+1,1))
    
        elif buy == 1:
            profit = max(0+getAns(ind+1,1),Arr[ind]+getAns(ind+1,0))
        return profit
    ans = getAns(0,0)
    return ans

def main():
    n = 6
    Arr = [7, 1, 5, 3, 6, 4]

    max_profit = getMaximumProfit(Arr, n)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()


#################### MEMORIZATION

def getMaximumProfit(Arr,n):

    if n==0:
        return 0
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    def getAns(ind,buy):

        if ind == n:
            return 0
        
        if dp[ind][buy]!=-1:
            return dp[ind][buy]
        profit = 0 
        if  buy == 0:
            profit = max(0+getAns(ind+1,0),-Arr[ind]+getAns(ind+1,1))
    
        elif buy == 1:
            profit = max(0+getAns(ind+1,1),Arr[ind]+getAns(ind+1,0))
        dp[ind][buy] = profit
        return profit
    ans = getAns(0,0)
    return ans

def main():
    n = 6
    Arr = [7, 1, 5, 3, 6, 4]

    max_profit = getMaximumProfit(Arr, n)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()


#############  TABULATION


def getMaximumProfit(Arr,n):

    dp = [[-1 for _ in range(2)] for _ in range(n+1)]
    
    dp[n][0] = dp[n][1] = 0

    for ind in range(n-1,-1,-1):

        for buy in range(2):
            profit  = 0
            
             
            if  buy == 0:
                profit = max(0+dp[ind+1][0],-Arr[ind]+dp[ind+1][1])
        
            elif buy == 1:
                profit = max(0+dp[ind+1][1],Arr[ind]+dp[ind+1][0])
            dp[ind][buy] = profit
            
    
    return dp[0][0]

    
        
def main():
    n = 6
    Arr = [7, 1, 5, 3, 6, 4]

    max_profit = getMaximumProfit(Arr, n)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()





##############  SPACE OPTIMIZATION


def getMaximumProfit(Arr,n):

   
    ahead = [0,0]
    cur = [0,0]
   
    ahead[0] = ahead[1] = 0
    for ind in range(n-1,-1,-1):

        for buy in range(2):
            profit  = 0
            
             
            if  buy == 0:
                profit = max(0+ahead[0],-Arr[ind]+ahead[1])
        
            elif buy == 1:
                profit = max(0+ahead[1],Arr[ind]+ahead[0])
            cur[buy] = profit
            
        ahead = cur
    return cur[0]

    
        
def main():
    n = 6
    Arr = [7, 1, 5, 3, 6, 4]

    max_profit = getMaximumProfit(Arr, n)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()