import time
from icecream import ic

# This program includes 4 different implementations of a Fibonacci number-generating algorithm
'''
# 1. Using a generator to generate Fibonacci numbers
def genTest():
    fib0 = 0
    fib1 = 1
    while True:
        next = fib0 + fib1
        yield next
        fib0 = fib1
        fib1 = next

count = 2
for n in genTest():
    print(f"Fibonacci number of {count}:",n)
    count += 1
    time.sleep(0.2)
'''

'''
# 2. Using dictionaries and recursion to generate Fibonacci numbers
def fibDict(n, d={0:0, 1:1, 2:1}):
    if n in d:
        return d[n]
    else:
        d[n]= fibDict(n-1,d) + fibDict(n-2,d)
        return d[n]

ic(fibDict(999)) # works for n = [1,999]
'''
'''
# 3. Using recursion alone to generate Fibonacci numbers
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

ic(fib(10)) # takes significantly longer for greater values of n
'''

# 4. Using pure iteration to generate Fibonacci numbers
def fib_iter(n):
    fib0 = 0
    fib1 = 1
    result = 0
    x = 1
    while x < n:
        result = fib0 + fib1
        x += 1
        fib0 = fib1
        fib1 = result
    return result

for n in range(10):
    ic(n, fib_iter(n))
    
# 5. DP implementation

def dp_fib(n):
    arr = [0] * n-1
    arr[0], arr[1] = 1,1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[1-2]
    return arr[n]
