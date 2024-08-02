# Example 1:
# Input:
#  intervals=[[1,3],[2,6],[8,10],[15,18]]

# Output:
#  [[1,6],[8,10],[15,18]]

# Explanation:
#  Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
#  intervals.


### BRute Force Method

# def merge(intervals):

#     intervals.sort()
#     n = len(intervals)
#     ans  = []

#     for i in range(n):
#         start , end  = intervals[i][0], intervals[i][1]
        
#         if ans and end<= ans[-1][-1]:
#             continue

#         for j in range(i+1,n):
#             if intervals[j][0] <= end :
#                 end = max(end, intervals[j][1])
#             else :
#                 break
#         ans.append([start,end])
#     return ans


# intervals=[[1,3],[2,6],[8,10],[15,18]]
# print(merge(intervals))


############ Optimal Approach    

def merge(intervals):

    n = len(intervals)

    intervals.sort()

    ans  = []

    for i in range(n):

        if not ans or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])

        else :
            ans[-1][i] = max(ans[-1][1], intervals[i][1])

    return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))