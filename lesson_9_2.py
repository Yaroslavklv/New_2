a='мальчик шел шел в школу и не дошел в школу'
a=list(a.split(' '))
print(a)
b=[]
for i in range(len(a)):
    b.append(a.count(a[i]))
print(b)
dic=dict(zip(a,b))
print(dic)