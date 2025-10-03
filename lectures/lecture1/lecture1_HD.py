"""
Part 2, Lecture 1

Implement and test argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns 
    the index (position) the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an 
    empty sequence.

4.  Use the notebook lecture1-benchmark.ipynb to benchmark your implementation 
    against NumPy's argmax().
"""
import numpy as np

def argmax(lst):
    n = len(lst)

    if n == 0:
        raise ValueError('Empty lists are not supported')

    value_max = - np.inf
    imax = 0

    for i in range(n):
        value = lst[i]
        if value > value_max:
            # Update index of largest element
            imax = i
            # Update the largest element
            value_max = value

    return imax

if __name__ == '__main__':
    #values = [2, 3, -1, 7, 4]
    values = []

    try:
        i = argmax(values)
        print(f'Index of max value: {i}')
    except ValueError:
        print('Empty list')