# Majority Elements(&gt;N/3 times) | Find the elements that appears more than N/3 times in the array
# Example 1:
# Input Format
# : N = 5, array[] = {1,2,2,3,2}
# Result
# : 2
# Explanation:
#  Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.

# ### this is brute force method .....
# def majorityelements(arr):
#     n = len(arr)

#     list = []
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[j] == arr[i]:
#                 count+=1
#         if count > (n//3):
#             list.append(arr[i])

#         if len(list) == 2:
#             break

#     return len(list)



# #Better solution but there is space complecity

# from collections import Counter
# def majorityelements(arr):
#     n = len(arr)

#     counter = Counter(arr)

#     for num,count in counter.items():
#         if count > (n//2):
#             return num
#     return -1


# optimal solution optimal

def optimalmajoritylement(arr):
    n = len(arr)

    cnt1 , cnt2 = 0,0
    el1,el2 = float('-inf'),float('-inf')

    for i in range(n):
        if cnt1 == 0 and el2 != arr[i]:
            cnt1 = 1
            el1 = arr[i]
        elif cnt2==0 and el1 != arr[i]:
            cnt2 = 1
            el2 = arr[i]
        elif arr[i] == el1:
            cnt1+=1
        elif arr[i] == el2:
            cnt2+=1
        else :
            cnt1-=1
            cnt2-=1

    ls = []

    cnt1,cnt2=0,0
    for i in range(n):
        if arr[i] ==  el1:
            cnt1+=1
        if arr[i] == el2:
            cnt2+=1
    mini = int(n/3)+1
    if cnt1 >=mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)

    return ls




arr = [2,2,1,1,1,2,2]
print(optimalmajoritylement(arr))

