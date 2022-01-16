import random

# a=[random.randint(150,200) for _ in range(10)]
a = [180, 167, 155, 178, 180, 190, 200]
x = int(input())
print(a)
a.append(x)
k = a.count(x)
# if k>1:

a.sort(reverse=True)

t = a.index(x)

b = t + 1
print(a, k, "index_", b)
