import random
a=[random.randint(1,20) for _ in range(10)]
b=[random.randint(1,20) for _ in range(10)]
a=a+b
a.sort()
a=[ch for ch in range(0,len(a)-1) if a[ch]!=a[ch-1] and a[ch]!=a[ch+1]]
print(len(a))
