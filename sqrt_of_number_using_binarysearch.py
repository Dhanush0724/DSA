#Finding Sqrt of a number using Binary Search
#Brute Force method
# def srt(n):
#     ans = 0
#     for i in range(1,n+1):
#         val = i*i
#         if val<=n:
#             ans = i 
#         else :
#             break
#     return ans
# print(srt(37))


##USing Binary Search Method

def sqrtceil(n):
    low = 1
    high = n-1

    while low <= high:
        mid = (low+high)//2
        val = mid*mid
        if val <= n:
            low = mid+1
        else :
            high = mid-1
    return high

print(sqrtceil(28))
