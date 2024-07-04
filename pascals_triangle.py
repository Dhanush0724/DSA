
# # # pascal's traingle
# # # Input Format:
# # #  N = 5, r = 5, c = 3
# # # Result:
# # #  6 (for variation 1)

# # import math


# # def nCr(n,r):
# #     res = 1

# #     for i in range(r):
# #         res = res*(n-i)
# #         res = res//(i+1)
# #     return res

# # def pascaltraingle(r,c):
# #     element = nCr(r-1,c-1)
# #     return element

# # if __name__ == '__main__':
# #     r = 5 # row number
# #     c = 3 # col number
# #     element = pascaltraingle(r, c)
# #     print(f"The element at position (r,c) is: {element}")

# # #
# # Input Format:
# #  N = 5, r = 5, c = 3
# # Result:

# # 1 4 6 4 1 (for variation 2)

# def pascaltriangle(n):
#     ans = 1
#     print(ans, end=" ")

#     for i in range(1,n):
#         ans = ans*(n-i)
#         ans = ans//i
#         print(ans,end=" ")
#     print()

# n = 5
# pascaltriangle(n)

# Input Format:
#  N = 5, r = 5, c = 3
# Result:
# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1    (for variation 3)


def generaterow(row):
    ans = 1
    ansRow = [1]

    for col in range(1,row):
        ans *= (row-col)
        ans  //= col
        ansRow.append(ans)
    return ansRow


def pascaltriangle(n):
    ans = []

    for row in range(1,n+1):
        ans.append(generaterow(row))
    return ans

if __name__ == "__main__":
    n = 5
    ans = pascaltriangle(n)
    for i in ans:
        for ele in i:
            print(ele,end=" ")
        print()




