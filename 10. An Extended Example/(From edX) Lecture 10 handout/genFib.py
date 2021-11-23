# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:44:36 2016

@author: ericgrimson

From Unit 5 (OOP), Chapter 10, Video 6 - Generators
"""
import time

def genFib():
    '''
    Inputs: none

    Returns a generator object which calculates the Fibonacci number of (n-1)
    in the generator's nth call.
    '''
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next # yield statement returns a generator object
        fibn_2 = fibn_1
        fibn_1 = next


fib = genFib()
# 1st 2 Fibonacci numbers are part of genFib() and will not be generated.

'''
# Iterating through the generator object through number range-based iteration
for n in range(10):
    print("fib number of", n+2,"is", fib.__next__())
'''


# Using the generator object alone to iterate infinitely
count = 2
for n in genFib():
    print("fib number of", count,"is", fib.__next__())
    count += 1
    time.sleep(0.5)
