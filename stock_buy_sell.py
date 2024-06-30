

# def stock(arr):
#     maxi = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[j] > arr[i]:
#                 maxi = max(arr[j] - arr[i],maxi)


#     return maxi

def stock(arr):

    maxi = 0
    minprice = float('inf')
    for i in range(len(arr)):
        minprice = min(minprice,arr[i])
        maxi = max(maxi,arr[i]-minprice)
    return maxi

arr = [7,1,5,3,6,4]
print(stock(arr))