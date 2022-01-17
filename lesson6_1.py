import random
a=[random.randint(120,200) for _ in range(10)]
x=int(input())
a.append(x)
a.sort(reverse=True)
print(a.index(x)+a.count(x))
