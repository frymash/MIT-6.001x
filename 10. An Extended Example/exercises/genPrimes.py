# Edited by ozervesh on Mon 29 Nov 2021

import time
from icecream import ic

def genPrimes():
    primes = []
    x = 1
    while True:
        x += 1
        for p in primes:
            if (x % p) == 0:
                break
        else:
            primes.append(x)
            yield x

# learning point from genPrimes() above - an else block will still be executed
# even if it's on a different indentation level as the if block as long as the
# if condition preceding it isn't met.

'''
My own ideation of genPrimes earlier (which works but is slower):

def genPrimes():
    primes = []
    x = 1
    while True:
        x += 1
        bool_check = []
        for p in primes:
            if (x % p) != 0:
                bool_check.append(True)
            else:
                bool_check.append(False)
        if False in bool_check:
            continue
        else:
            primes.append(x)
            yield x
'''

for x in genPrimes():
    print(x)
    time.sleep(0.5)