'''
PROBLEM STATEMENT:

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

`Longest substring in alphabetical order is: beggh`

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

`Longest substring in alphabetical order is: abc`

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you 
move on to a different part of the course. If you have time, come back to 
this problem after you've had a break and cleared your head.
'''

s = 'ttifipjrif'
s = s.lower()
substr = ''
substr_list = []

for i in range(len(s)):
    if s[i] > s[i+1] or i == len(s)-1:
        if s[i] >= s[i-1]:
            substr += s[i]
        substr_list.append(substr)
        substr = ''
        
    elif s[i] <= s[i+1]:
        substr += s[i]

print('Longest substring in alphabetical order is:', max(substr_list, key=len))
