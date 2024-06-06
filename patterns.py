n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
        i+=1
    print()
print("///////////////////////")
for i in range(1,n):
    for j in range(i):
        print(i,end="")
    print()
print("////////////////")
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print("///////////////////")
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("///////////////////////////////")
print("full pyramid")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
print("reverse pyramid")
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end = "")
    print()
print("///////////////////")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end = "")
    print()
print("/////////////////")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for j in range(i+1):
        print("*",end="")
    print()
print("///////////////")

for i in range(n):
    for j in range(i+1):
        if (i+j)%2==0:
            print("1",end="")
        else :
            print("0",end="")
    print()