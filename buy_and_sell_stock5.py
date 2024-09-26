###############   COOLDOWN  (can't buy right after the sell)



def get_max_profit(prices, ind, buy, n, dp):
    
    if ind >= n:
        return 0


    if dp[ind][buy] != -1:
        return dp[ind][buy]

    # Initialize profit
    profit = 0

    if buy == 0:  # We can buy the stock
        profit = max(
            0 + get_max_profit(prices, ind + 1, 0, n, dp),
            -prices[ind] + get_max_profit(prices, ind + 1, 1, n, dp)
        )

    if buy == 1:  # We can sell the stock
        profit = max(
            0 + get_max_profit(prices, ind + 1, 1, n, dp),
            prices[ind] + get_max_profit(prices, ind + 2, 0, n, dp)
        )

    # Memoize the result and return
    dp[ind][buy] = profit
    return profit


def stock_profit(prices):
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n)]

    ans = get_max_profit(prices, 0, 0, n, dp)
    return ans


if __name__ == "__main__":
    prices = [4, 9, 0, 4, 10]

    result = stock_profit(prices)
    print(f"The maximum profit that can be generated is {result}")



#### TABULATION

def stock_profit(prices):

    n = len(prices)

    dp = [[0 for _ in range(2)] for _ in range(n+2)]

    for ind in range(n-1,-1,-1):
        for buy in range(2):
            profit  = 0

            if buy == 0:  
                profit = max(
                    0 + get_max_profit(prices, ind + 1, 0, n, dp),
                    -prices[ind] + get_max_profit(prices, ind + 1, 1, n, dp)
                )

            if buy == 1:  
                profit = max(
                    0 + get_max_profit(prices, ind + 1, 1, n, dp),
                    prices[ind] + get_max_profit(prices, ind + 2, 0, n, dp)
                )

            dp[ind][buy] = profit

    return dp[0][0]
            


if __name__ == "__main__":
    prices = [4, 9, 0, 4, 10]

    result = stock_profit(prices)
    print(f"The maximum profit that can be generated is {result}")
