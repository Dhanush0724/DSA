
V = 49
coins  = [1,2,5,10,20,50,100,200,500,2000]
ans  = []
n= 10

for i in range(n-1,-1,-1):
    while V >= coins[i]:
        V -= coins[i]
        ans.append(coins[i])


print(ans)