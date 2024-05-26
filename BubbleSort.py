
def BubbleSort(list):

    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

list = [6,9,2,3,4,5]
BubbleSort(list)
print(list)