def arithmetic (a,b,c):
"""
Nev function performs algebraic operations on argument 1 and argument 2, depending on the specified operation:
addition, subtraction, multiplication and division.
If another operation is entered, then the line "Unknown operation" is displayed.
:type a:int
:type b:int
:tepe c:str
:param a: argument 1
:param b: argument 2
:param c: specified operation
:return int and str

"""
a=int(input())
b=int(input())
c=input()
alg={"+":a+b, "-":a-b, "*":a*b, "/":a/b}
if alg.get(c):
    print(alg[c])
else:
    print("Неизвестная операция")
return alg[c], print("Неизвестная операция")
