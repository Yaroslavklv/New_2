def function_remainder(x):
    temp=1
    while x!=0:
        t = x % 10
        if t>0:
            temp*=t
        x=x//10
    return temp
print(function_remainder(int(input())))
