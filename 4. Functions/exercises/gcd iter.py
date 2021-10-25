def gcdIter(a, b):
    '''
    a, b: positive integers. Let b always be the smaller int.
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testVal = b if b < a else a
    for ans in range(testVal, 0, -1):
        if a % ans == 0 and b % ans == 0:
            return ans


# testing
# print(gcdIter(2,12)) # Answer: 2
# print(gcdIter(6,12)) # Answer: 6
# print(gcdIter(9,12)) # Answer: 3
# print(gcdIter(17,12)) # Answer: 1

'''
INSTRUCTIONS:

Write an iterative function, gcdIter(a, b), that finds the GCD 
of 2 ints through iteration. One easy way to do this is to begin 
with a test value equal to the smaller of the two input arguments, 
and iteratively reduce this test value by 1 until you either reach a case 
where the test divides both a and b without remainder, or you reach 1.
'''
