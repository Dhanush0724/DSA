import heapq

H = [21,4,45,87,6,2]
# use heapify to rearrange the elements
heapq.heapify(H)
print(H)

# add element
heapq.heappush(H,8)
print(H)

#remove element from the heap
heapq.heappop(H)
print(H)

#replace the smallest element in list
heapq.heapreplace(H,6)
print(H)


# joing merging two heaps
J = [2,65,98,655,3,5,35]
merged = list(heapq.merge(H,J))
print(merged)

print(heapq.nsmallest(1,H))
print(heapq.nlargest(3,J))