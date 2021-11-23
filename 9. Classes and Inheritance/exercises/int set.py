#!/usr/local/bin python3

'''
INSTRUCTIONS: 
1. Define an intersect method that returns a new intSet containing 
elements that appear in both sets. In other words, s1.intersect(s2)
would return a new intSet of integers that appear in both s1 and s2. 
Think carefully - what should happen if s1 and s2 have no elements in common?

2. Add the appropriate method(s) so that len(s) 
returns the number of elements in s. 
'''

from icecream import ic

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        '''
        Inputs: 
        other - another intSet object

        Returns: 
        a new intSet object containing elements common to 'self' and other'
        '''
        commonVals = intSet()
        for e in self.vals:
            if e in other.vals:
                commonVals.vals.append(e)
        return commonVals
        # return commonVals if commonVals.vals else None

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


    def __len__(self):
        '''
        Returns:
        length of self.vals within an intSet() instance

        This method is called by the len() built-in method.
        '''
        return len(self.vals)

# Creating new intSet objects in preparation for testing
test1 = intSet()
for n in range(10):
    test1.insert(n)
print("Test1:", test1) # {0,1,2,3,4,5,6,7,8,9}

test2 = intSet()
for n in [10,12,14,16]:
    test2.insert(n)
print("Test2:", test2) # {10,12,14,16}

test3 = intSet()
for n in [0,1,40,50,60]:
    test3.insert(n)
print("Test3:", test3) # {0,1,40,50,60}

test4 = intSet() # Empty set
print("Test4:", test4) # {}

test5 = intSet() # Empty set
print("Test5:", test5) # {}

# Testing the intersect method via black box testing (based on docstr)

# 1. Intersecting 2 empty sets
print("Common elements bt. test4 and test5:", test4.intersect(test5)) # {}
# 2. Intersecting an empty set with a non-empty set
print("Common elements bt. test3 and test4:", test3.intersect(test4)) # {}
# 3. Intersecting 2 non-empty sets without any common elements
print("Common elements bt. test1 and test2:", test1.intersect(test2)) # {}
# 4. Intersecting 2 non-empty sets with >=1 common element
print("Common elements bt. test1 and test3:", test3.intersect(test1)) # {0,1}


# Testing the __len__ method via black box testing (based on docstr)

# 1. Length of an intSet object where len(self.vals) == 0
print("Length of test4:", len(test4)) # 0
# 2. Length of an intSet object where len(self.vals) != 0
print("Length of test1:", len(test1)) # 10
