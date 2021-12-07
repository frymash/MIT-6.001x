# MIT 6.001x Problem Set 6

7/12/2021 note: 
The answers below have been checked and these are the correct answers

Questions which were incorrectly answered on the first attempt:
- 4-1 - I picked O(log(n)) instead of the correct O(1) due to the modulo.
- 6-3 - I picked `No change.` when the answer was `modSwapSort now orders the list in descending order for all lists.`

## Problem 1
|No.|Question|Answer|
|---|--------|------|
|1-1|The ONLY thing we are interested in when designing programs is that it returns the correct answer.|False|
|1-2|When determining asymptotic complexity, we discard all terms except for the one with the largest growth rate.|True|
|1-3|Bisection search is an example of linear time complexity.|False|
|1-4|For large values of `n`, an algorithm that takes `20000n^2` steps has better time complexity (takes less time) than one that takes `0.001n^5` steps|True|


## Problem 2
|No.|Question|Answer|
|---|--------|------|
|2-1|Indirection, as talked about in lecture, means you have to traverse the list more than once.|False|
|2-2|The complexity of binary search on a sorted list of n items is O(log(n)).|True|
|2-3|The worst case time complexity for selection sort is O(n^2)|True|
|2-4|The base case for the recursive version of merge sort from lecture is checking ONLY for the list being empty.|False|


## Problem 3

For each of the following expressions, select the order of growth class that best describes it from the following list: O(1),O(log(n)), O(n), O(n log(n)), O(n^c) or O(c^n). Assume c is some constant.

|No.|Question|Answer|
|---|--------|------|
|3-1|`0.0000001n + 1000000`|O(n)|
|3-2|`0.0001n^2 + 20000n - 90000`|O(n^c)|
|3-3|`20n + 900 log(n) + 100000`|O(n)|
|3-4|`(log(n))^2 + 5n^7`|O(n^c)|
|3-5|`n^200 - 2n^30`|O(n^c)|
|3-6|`30n^2 + n log(n)`|O(n^c)|
|3-7|`n log(n) - 3000n`|O(n log(n)|
|3-8|`3`|O(1)|
|3-9|`5^n + n^5 + n + 5`|O(c^n)|
|3-10|`n log(n) + n^2 + n + log(n) + 1 + 2^n`|O(c^n)|


## Problem 4
|No.|Answer|
|---|------|
|4-1|O(1)|
```python
def modten(n):
    return n%10
```


|No.|Answer|
|---|------|
|4-2|O(len(n))|
```python
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result
```


|No.|Answer|
|---|------|
|4-3|O(log(n))|
```python
def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1
```


|No.|Answer|
|---|------|
|4-4|O(n)|
```python
def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)
```


|No.|Answer|
|---|------|
|4-5|O(n^2)|
```python
def baz(n):
    for i in range(n):
        for j in range(n):
            print( i,j )
```

## Problem 5

Here is code for linear search that uses the fact that a set of elements is sorted in increasing order:
```python
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
```

Consider the following code, which is an alternative version of `search`.

```python
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
```
Which of the following statements is correct? You may assume that each function is tested with a list `L` whose elements are sorted in increasing order; for simplicity, assume `L` is a list of positive integers.


|No.|Answer|
|---|------|
|5|`search` and `newsearch` return the same answers for lists L of length 0, 1, or 2.|


## Problem 6

Answer the questions below based on the following sorting function. If it helps, you may paste the code in your programming environment. Study the output to make sure you understand the way it sorts.

```python
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
```

|No.|Question|Answer|
|---|--------|------|
|6-1|Does this function sort the list in increasing or decreasing order?|Increasing|
|6-2|What is the worst case time complexity of swapSort? Consider different kinds of lists when the length of the list is large.|O(n^2)|


If we make a small change to the line `for j in range(i+1, len(L))`: such that the code becomes:
```python
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
```


|No.|Question|Answer|
|---|--------|------|
|6-3|What happens to the behavior of `swapSort` with this new code?|`modSwapSort` now orders the list in descending order for all lists.|
|6-4|What happens to the time complexity of this `modSwapSort?`|Best and worst cases stay the same.|
