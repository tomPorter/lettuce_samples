def factorial(number):
    """ factorial x.

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
