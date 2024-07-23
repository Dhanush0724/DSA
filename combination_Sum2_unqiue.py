

## Unqiue combination

def combinationsum(candidates,target):
    res = []
    ds = []
    candidates.sort()

    def findcombination(ind,target):
        if target == 0:
            res.append(ds[:])
            return
        for i in range(ind,len(candidates)):
            if i > ind and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            ds.append(candidates[i])
            findcombination(i+1,target-candidates[i])
            ds.pop()
    findcombination(0,target)
    return res

if __name__ == "__main__":
    v = [10, 1, 2, 7, 6, 1, 5]
    comb = combinationsum(v, 8)
    print(*comb)