# Example 1:

# Input: height= [0,1,0,2,1,0,1,3,2,1,2,1]

# Output: 6

# Explanation: As seen from the diagram 1+1+2+1+1=6 unit of water can be trapped


###BRute force method

# def trap(arr):
#     n = len(arr)
#     waterTrapped = 0
#     for i in range(n):
#         j = i
#         leftmax = 0
#         rightmax  = 0
#         while j >=0 :
#             leftmax = max(leftmax,arr[j])
#             j -=1
#         j = i

#         while j<n:
#             rightmax = max(rightmax,arr[j])
#             j +=1            
#         waterTrapped += min(leftmax,rightmax) - arr[i]
#     return waterTrapped

# if __name__ == "__main__":
#     arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#     print(f"The water that can be trapped is {trap(arr)}")


# Optimal  two pointer

def trap(height):
    n = len(height)
    left = 0
    right = n-1
    res = 0
    maxleft = 0
    maxright = 0
    while left<=right:
        if height[left] <= height[right]:
            if height[left] >= maxleft:
                maxleft = height[left]
            else :
                res += maxleft - height[left]
            left +=1
        else :
            if height[right] >= maxright:
                maxright = height[right]
            else :
                res += maxright - height[right]
            right -=1
    return res
    
if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")