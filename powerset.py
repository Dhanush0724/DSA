
# Example 1:
# Input: str = "abc"
# Output: a ab abc ac b bc c
# Explanation: Printing all the 7 subsequence for the string "abc".

def solve(i,s,f):
    if i == len(s):
        print(f, end= " ")
        return
    
    solve(i+1,s,f+s[i])
    solve(i+1,s,f)

s = "abc"
f = ""
print("All possible subsequence are:")
solve(0,s,f)
        