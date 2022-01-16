import random

# a=[random.randint(150,200) for _ in range(10)]
a = [181, 167, 155, 178, 182, 190, 200]
x = int(input())
print(a)
a.append(x)
k = a.count(x)
a.sort(reverse=True)
t = a.index(x)
print(a, k, "index_", t+1)


#if k>1:
#   a.insert((a.index(x)-k),x)

#else:



#a.pop(t-1)
#b = t + 1

