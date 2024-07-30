

def cookies(g,s):

    g.sort()
    s.sort()
    l = 0
    r = 0
    n = len(g)
    m = len(s)
    while(l<m and r<n):
        if (g[r] <= s[l]):

            r+=1
        l+=1
    return r


g = [1,5,3,3,4]
s = [4,2,1,2,1,3]
print(cookies(g,s))