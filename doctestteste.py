import doctest

# def average(values):
#     """Computes the arithmetic mean of a list of numbers.

#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)

def square(x):
    '''
    >>> square(2)
    4
    '''
    return x**2


y = doctest.testmod()
print(y)