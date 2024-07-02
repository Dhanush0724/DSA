def longestsuccessiveelements(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    longest = 1
    st = set()

    for i in range(n):
        st.add(arr[i])

    for i in st:
        if i -1 not in st:

            cnt = 1
            x = i
            
            while x+1 in st:
                x+=1
                cnt+=1
            longest =  max(longest, cnt)
    return longest


arr = [100,200,1,2,3,4]
print(longestsuccessiveelements(arr))