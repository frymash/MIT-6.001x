def fib(n):
    '''
    n : a non-negative int

    returns the Fibonacci number of n
    '''
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_dict(n,d):
    '''
    n : a non-negative int
    d : a dictionary containing all the Fibonacci numbers calculated so far
    {key:value} -> {n:fib(n)}
    '''
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_dict(n-1,fib_dictionary) + fib_dict(n-2,fib_dictionary)
        d[n] = ans
        return ans


# Calculating fib(n) for n = 1 to n = 30
numFibCalls = 0

for i in range(32):
    print('n =',i,'| Fib number:',fib(i))
print('Number of fib(n) calls:',numFibCalls)

# Calculating fib_dict(n) for n = 1 to n = 30

numFibCalls = 0
fib_dictionary = {0:1,1:1} # key -> n, value -> fib(n)

for i in range(32):
    print('n =',i,'| Fib number:',fib_dict(i,fib_dictionary))
print('Number of fib(n) calls:',numFibCalls)
