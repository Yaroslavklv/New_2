a=int(input())
b=int(input())
c=input()

alg={"+":a+b, "-":a-b, "*":a*b, "/":a/b}

if alg.get(c):
    print(alg[c])
else:
    print("Неизвестная операция")

