# #Optimal approach
# import math

# def findMax(v):
#     maxi = float('-inf')
#     n = len(v)

#     for i in range(n):
#         maxi = max(maxi,v[i])
#     return maxi

# def calaculatetotalhours(v,hourly):
#     totalH = 0
#     n = len(v)

#     for i in range(n):
#         totalH += math.ceil(v[i]/hourly)
#     return totalH

# def minimumratetoeatbananas(v,h):
#     maxi = findMax(v)

#     for i in range(1,maxi+1):
#         reqtime = calaculatetotalhours(v,i)
#         if reqtime <= h:
#             return i
        
#     return maxi



# v = [7,15,6,3]
# h= 8
# print(minimumratetoeatbananas(v,h))

import math

def findMax(v):
     maxi = float('-inf')
     n = len(v)
     for i in range(n):
          maxi = max(maxi,v[i])
     return maxi

def calculatehours(v,hourly):
     total = 0
     n = len(v)

     for i in range(n):
          total += math.ceil(v[i]/hourly)
     return total

def minimumratetoeatbananas(v,h):
     low = 1
     high = findMax(v)
     ans = 0
     while low<=high:
          mid = (low+high)//2

          totalH = calculatehours(v,mid)
          if totalH<=h:
               ans = totalH
               high = mid-1
          else :
               low = mid+1
     return low
          
    
    


v = [7,15,6,3]
h= 8
print(minimumratetoeatbananas(v,h))