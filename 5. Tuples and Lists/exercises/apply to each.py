# function f is applied to each element in list L
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

'''
# apply to each 1 (goal: testList = [1, 4, 8, 9])
# Absolute value function
def abs(a):
    return -a if a <0 else a

applyToEach(testList, abs)
# print(testList)
'''

'''
# apply to each 2 (goal: testList = [2, -3, 9, -8])
# Incrementing function
def inc(a):
    a += 1
    return a

applyToEach(testList, inc)
# print(testList)
'''

# apply to each 3 (goal: testList = [1, 16, 64, 81])
# Square function
def square(a):
    return a*a
    
applyToEach(testList,square)
# print(testList)
