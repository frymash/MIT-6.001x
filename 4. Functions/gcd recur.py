def gcdRecur(a, b):
    '''
    a, b: positive integers. Let b always be the smaller int.
    
    returns: a positive integer, the greatest common divisor of a & b.

    Take note of Euclid's algorithm to find the GCD: 
    https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
    '''
    (a,b) = (a,b) if a > b else (b,a)
    if a % b == 0:
        return b
    else:
        return gcdRecur(b, a % b)

# testing
# print(gcdRecur(2,12)) # Answer: 2
# print(gcdRecur(1071,462)) # Answer: 21
# print(gcdRecur(3,63)) # Answer: 3
# print(gcdRecur(17,12)) # Answer: 1

'''
The following code is the answer provided by MIT:


def gcdRecur(a, b):

    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)

22/10/2021 - Some personal notes after running both answers through pythontutor.com:

    The provided answer is seemingly slightly less efficient than my answer. 
    It does, however, take up less space compared to my answer and feels 
    a lot more elegant.

    For the problem of finding the GCD of 2 ints, a recursive approach is also
    more efficient than an iterative solution. Example: for the numbers 1071 and
    462, finding the GCD would take 1000+ steps with an iterative approach. With
    a recursive approach, however (regardless of whether it's my ans or the MIT ans),
    only takes about 30-40+ steps to find the GCD. 
'''

'''
INSTRUCTIONS:

A clever mathematical trick (due to Euclid) makes it easy to find greatest 
common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example for an 
example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. 
This function takes in two positive integers and returns one integer.
'''