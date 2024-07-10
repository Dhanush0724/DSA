

def CountStudents(books,mid):
    n = len(books)
    student = 1
    pages = 0
    for i in range(n):

        if pages+books[i] <= mid:
            pages += books[i]
        else :
            student +=1 
            pages = books[i]
    return student

def minimumpagesallocate(books,n,m):

    if m>n:
        return -1
    
    low = max(books)
    high = sum(books)
    while low<=high:

        mid = (low+high)//2

        students = CountStudents(books,mid)

        if students>m:
            low = mid+1
        else :
            high = mid-1
    return low

   

books = [25,46,28,49,24]
n = 5
m = 4
print(minimumpagesallocate(books,n,m))