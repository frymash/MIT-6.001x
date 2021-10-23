'''
PROBLEM STATEMENT:
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

`Number of times bob occurs is: 2`
'''
s = 'azcbobobegghakl'


# Method 1: Use RegEx
from re import findall
print('Number of times bob occurs is:', len(findall('b(?=ob)',s)))

'''
# Method 2: Counting through iteration and string indexing
bobs = 0
for i in range(len(s)-3):
    if s[i:i+3] == 'bob':
        bobs += 1
print('Number of times bob occurs is:', bobs)
'''
