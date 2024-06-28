from collections import  Counter

def check(arr,n):

    
    counter = Counter(arr)
    
    for num,count in counter.items():
        if count >(n//2):
            return num

arr = [3,2,3,2,2,2]
n = 6
print(check(arr,n))