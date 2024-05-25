def add(n):
    if len(n) == 1:
        return n[0]
    else :
        return n[0] + add(n[1:])
if __name__ == "__main__":
    print(add([1,2,3,4,5,6,7,8,9]))


def convert(n,base):
    convert_string = "0123456789ABCDEF"

    if n<base:
        return convert_string[n]
    else :
        return convert_string[n%base] + convert(n//base,base)
    
print(convert(2835,16))

def recursive_list(data):
    total = 0
    for elements in data:
        if type(elements) == type([]):
            total = total + recursive_list(elements)
        else :
            total = total +elements

    return total

print(recursive_list([1,2,[3,4],[5,6]]))

def factorial(num):
    if num <= 1:
        return 1
    else :
        return num * factorial(num-1)
    
print(factorial(5))

def fib(nu):
    if nu== 1 or nu==2:
        return 1
    else :
        return fib(nu-1) + fib(nu-2)
    
print(fib(3))

def sum(digit):
    if digit== 0:
        return 0
    else :
        return digit % 10 +sum(int(digit//10))
print(sum(345))

def series(x):
    if x < 1:
        return 0
    else :
        return x + series(x-2)
series(6) 

def power(a,b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else :
        return a * power(a,b-1)
print(power(3,4))


def recurgdc(a,b):
    low = min(a,b)
    high = max(a,b)
    if low == 0 :
        return high
    elif low == 1:
        return 1
    else :
        return recurgdc(low,high%low)
print(recurgdc(12,14))