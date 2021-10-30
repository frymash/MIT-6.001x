def fib_efficient(n, dict):
    if n in dict:
        return dict[n]
    else:
        ans = fib_efficient(n-1,dict) + fib_efficient(n-2,dict)
        dict[n] = ans
        return ans

# key -> a number, n
# value - > answer to fib(n)
dict = {1:1,2:2}

testNum = int(input('Fill in the blank: I want to find the __th Fibonacci number - '))
print(f'Fibonacci number {testNum} is',fib_efficient(testNum,dict))
