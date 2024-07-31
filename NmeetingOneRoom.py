

def maxmeeting(n,start,end):

    # meet = [(start[i],end[i]) for i in range(n)]
    # meet.sort(key = lambda x :x[1])
    # return meet

    meet = sorted(zip(start,end), key = lambda x: x[1])
    
    selected_meeting =[]
    
    last_end_time = 0

    for i in range(n):

        if meet[i][0] >= last_end_time:
            selected_meeting.append(i+1)
            last_end_time = meet[i][1]
    return selected_meeting




n = 6
start = [1,3,0,5,8,5]
end  = [2,4,5,7,9,9] 
print(maxmeeting(n,start,end))