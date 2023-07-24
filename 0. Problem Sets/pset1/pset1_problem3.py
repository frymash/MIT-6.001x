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

for i, letter in enumerate(s):

    if i == len(s)-1 or letter > s[i+1]:
        
        if letter >= s[i-1]:
            substr += letter
        substr_list.append(substr)
        substr = ''
        
    elif letter <= s[i+1]:
        substr += letter

print('Longest substring in alphabetical order is:', max(substr_list, key=len))
