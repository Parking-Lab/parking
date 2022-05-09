'''
Author: Reid Dye

This file shows how all files should be documented.
This area should have a description of the file's contents.
'''

def divide(numerator: 'int|float', denomerators: 'list[int|float]', integer: 'bool' = True) -> 'list[int|float]':
    """divides numerator by all of the numbers in divisors

    Args:
        numerator (int|float): the number to be divided
        denomerators (list): a list of numbers to divide `numerator` by
        integer (bool, optional): use integer division, if true. Defaults to True.

    Raises:
        AssertionError: raises an error if you try to divide by zero.

    Returns:
        list: the list of numbers from dividing numerator by all of the denomerators
    """

    #TODO: make this error message more helpful
    assert not 0 in denomerators, "panic! aaaaaah! something bad happened!" #check for illegal inputs

    if integer:
        return [numerator//d for d in denomerators] # if integer is true, use integer division,
    return [numerator/d for d in denomerators]      # otherwise use normal division
