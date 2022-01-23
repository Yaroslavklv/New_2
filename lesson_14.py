def arithmetic (a, b, c):
    """
    Function for finding algebraic expressions for a square: the perimeter of the square,
    the area of the square and the diagonal of the square
    :type x:int
    :param a: side of a square
    :return: calculation result: perimeter, area, square diagonal
    """
    if c=="+":
        c=a+b
    elif c=="-":
        c=a-b
    elif c=="*":
        c=(a*b)
    elif c=="/":
         c=a/b
    else:
        print ("Неизвестная операция")
    return c
print(arithmetic(5,6,"*"))
