# # Example 1:
# # Input:
# #  nums = [-1,0,1,2,-1,-4]

# # Output:
# #  [[-1,-1,2],[-1,0,1]]

# # Explanation:
# #  Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

# #Brute force method
# def threesumbrute(arr):
#     n= len(arr)
#     s = set()
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if arr[i]+arr[j]+arr[k] == 0:

#                     temp = [arr[i],arr[j],arr[k]]
#                     temp.sort()
#                     s.add(tuple(temp))
#     return s

# arr = [-1,0,1,2,-1,-4]
# print(threesumbrute(arr))
# ans = threesumbrute(arr)
# for it in ans: 
#     print("[",end=" ")
#     for i in it:
#         print(i,end=" ")
#     print("]",end="")
# print("\n")

##Optimal solution OPTIMAL

def triplet(arr):
    n = len(arr)
    ans = []
    arr.sort()

    for i in range(n):

        if i!=0 and arr[i] == arr[i-1]:
            continue

        j = i+1
        k = n-1
        while j<k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum <0:
                j+=1
            elif total_sum> 0:
                k-=1
            else :
                temp = [arr[i],arr[j],arr[k]]
                ans.append(temp)
                j+=1
                k-=1


                while j<k and arr[j] == arr[j-1]:
                    j +=1 
                while j<k and arr[k] == arr[k+1]:
                    k-=1
    return ans
    
arr = [-1,0,1,2,-1,-4]

ans = triplet(arr)
for it in ans: 
    print("[",end=" ")
    for i in it:
       print(i,end=" ")
    print("]",end="")
print("\n")

        

