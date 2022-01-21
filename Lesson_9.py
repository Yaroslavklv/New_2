#a='Одним із ефективних шляхів вирішення поставленої проблеми є застосування комплексної системи, ' \
#  'яка використовує відновлювані джерела енергії, а саме сонячну енергію та геотермальну енергію'
a='один раз мальчик пошел пошел в школу один раз раз'
b=list(a.split(' '))
#name={'d':23, 'v':45, 'H':5}
dic={}
sum=1
for index, value in enumerate(b):
  dic[index]=value
print(dic)
for key, value in dic.items():
   print(value)
   
print

#for i in [list(a.split(' '))]:
#    b[i]+=1
#    print (f'KEY:{key}', f'V:{value}')
#b.fromkeys([1,2,3],'a')
#print (b)
#for i, t in enumerate(b):
#    print(f'{i} -{t}')
#    for j in range(1,23):

#name = dict(j=b[i])
#print (name)