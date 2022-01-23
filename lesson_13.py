def square (a):
    """
    Function for finding algebraic expressions for a square: the perimeter of the square,
    the area of the square and the diagonal of the square
    :type x:int
    :param a: side of a square
    :return: calculation result: perimeter, area, square diagonal
    """
    perimeter=a*4
    area=a*a
    diagonal=a*(2**(1/2))
    return perimeter, area, diagonal
print(square(int(input())))