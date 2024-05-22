
def hash_function(value):
    sum  = 0
    for char in value:
        sum += ord(char)
    
    return sum%10

print("james had hash code:",hash_function('James'))

