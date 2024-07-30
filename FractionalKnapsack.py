

def Fractionalknapsack(n,w,values,weight):

    ratio = [(values[i]/weight[i],values[i],weight[i]) for i in range(n) ]

    ratio.sort(key = lambda x:x[0], reverse=True)
    
    current_weight  = 0
    current_value = 0

    for r ,values,weight in ratio:
        if current_weight +weight <= w:
            current_weight+=weight
            current_value += values
        else :
            remain = w-current_weight
            current_value += values*(remain/weight)
            break
    return current_value




n = 3
w  = 50
values  = [100,60,120]
weight = [20,10,30]
print(Fractionalknapsack(n,w,values,weight))
