import random
a=[random.randint(1,20) for _ in range(10)]
b=[random.randint(1,20) for _ in range(10)]
c=(a+b)
c.sort()
c=[ch for ch in range(0,len(c)-1) if c[ch]!=c[ch-1] and c[ch]!=c[ch+1]]
print(len(c))
