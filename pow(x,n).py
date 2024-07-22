

#### Brute Force MEthod

# def pow(x,n):
#     ans = 1.0
#     for i in range(n):
#         ans = ans *x
#     return ans

## Optimal Approach Binary Exponentitation

def pow(x,n):
    ans = 1.0
    nn = n
    if n < 0:
        nn = -1*nn
    while nn:
        if nn %2:
            ans = ans*x
            nn = nn -1
        else :
            x = x*x
            nn = nn // 2
    if n <0:
        ans = 1.0/ans
    return ans


print(pow(2,10))