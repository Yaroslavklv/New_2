b='Это строка в которую {a} новую строку'.format(a=input())
print(b)
b='Это строка в которую {a} новую строку'.format(a='замена в строке')
print(b)
print(len(b))
if b.count('строка'):
    print('Да')
else:
    print('НЕТ')
