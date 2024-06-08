# string,letter = input().split()
# count = 0
# for char in string:
#     if letter==char:
#         count+=1
# print(count)
# print("////////////////////")

def reverse(sentence):
    words = sentence.split()
    reverse = [word[::-1] for word in words]
    return ' '.join(reverse)

print(reverse("let's take codingclub contest"))