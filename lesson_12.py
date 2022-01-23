def multiplication_by_number(x):
    """
    The function divides the number by the bit depth and multiplies each bit length of the number among themselves
    :type x:int
    :param x: positive integer
    :return: calculation result
    """
    temp=1
    while x!=0:
        t = x % 10
        if t>0:
            temp*=t
        x=x//10
    return temp
print(multiplication_by_number(int(input())))
