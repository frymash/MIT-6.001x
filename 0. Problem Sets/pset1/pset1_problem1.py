'''
PROBLEM STATEMENT:
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

`Number of vowels: 5`
'''
s = 'azcbobobegghakl'

# Method 1: Use RegEx
from re import findall
print('Number of vowels:', len(findall('[aeiou]',s)))

'''
# Method 2: Counting through iteration
vowel_num = 0
vowels = ['a','e','i','o','u']
for letter in s:
    if letter in vowels:
        vowel_num += 1
print('Number of vowels:', vowel_num)
'''
