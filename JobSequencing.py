

def JobSequencing(n,jobs):

    jobs.sort(key = lambda x: x[2], reverse = True)

    maxi = jobs[0][1]
    for i in range(1,len(jobs)):

        maxi = max(maxi,jobs[i][1])
    
    slot = [-1] *(maxi+1)
    countjobs = 0
    jobprofit = 0

    for i in range(len(jobs)):
        for j in range(jobs[i][1],0,-1):
            if slot[j] == -1:
                slot[j] = i
                countjobs+=1
                jobprofit += jobs[i][2]
                break

                        
    return countjobs, jobprofit



n = 4
jobs = [(1,4,20),(2,1,10),(3,2,40),(4,2,30)]
print(JobSequencing(n,jobs))