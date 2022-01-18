import random
a=[random.randint(1,200) for _ in range(10)]
a=[ch for ch in range(1,len(a)-1) if a[ch] > a[ch-1] and a[ch]>a[ch+1]]
print(len(a))