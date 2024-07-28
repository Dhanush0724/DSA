##### Brute Force Method
# def maxcards(cardpoints,k):
#      n = len(cardpoints)
#      max_points = 0
#      for i in range(k+1):
#           left_sum = sum(cardpoints[:i])
#           rigtht_sum = sum(cardpoints[n-(k-i):])
#           max_points = max(max_points,left_sum+rigtht_sum)
#      return max_points

def maxcards(cardpoints,k):
    l = 0
    r = len(cardpoints) - k
    total = sum(cardpoints[r:])
    res = total

    while r<len(cardpoints):

        total += (cardpoints[l] - cardpoints[r])
        res = max(res,total)
        l +=1
        r +=1
    return res


cardpoints = [1,2,3,4,5,6,1]
k= 3
print(maxcards(cardpoints,k))