#### set matrix equalls to zero

def markrow(matrix,n,m,i):

    for j in range(m):
        if matrix[i][j]!=0:
            matrix[i][j] = -1
def marcol(matrix,n,m,j):

    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def zeromatrix(matrix,n,m):

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markrow(matrix,n,m,i)
                marcol(matrix,n,m,j)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    n = len(matrix)
    m = len(matrix[0])
    ans = zeromatrix(matrix,n,m)

    print("The final matrix is :")
    for row in ans:
        for ele in row:
            print(ele,end=" ")
        print()