
l1 = [1, 2, 3, 4, 5, 6]
print(l1[3])
print(l1[-3])
print(l1[2:5])
print(l1[5:2:-1])
l1.reverse()
print(l1)
print(l1[::-1])
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

tree = [5, [], []]
tree[1] = [3, [], []]
