from icecream import ic

# This program includes 2 different implementations of a factorial number algorithm

# 1. Using iteration
def fact_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for n in range(10):
    ic(n, fact_iter(n))

'''
# 2. Using recursion
def fact_recur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recur(n-1)

for n in range(100):
    ic(n, fact_recur(n))
'''