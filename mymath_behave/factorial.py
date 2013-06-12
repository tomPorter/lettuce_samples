def factorial(number):
    """ factorial x.
    Returns factorial of x

    >>> factorial(0)
    1

    >>> factorial(1)
    1

    >>> factorial(4)
    24
    """
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number - 1)
        #return number*
def main():
    """docstring for main"""
    print factorial(5)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #main()
