# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:14:58 2016

@author: ericgrimson

From Unit 5 (OOP), Chapter 10, Video 3 - Adding Another Class
"""

from MITPersonModifiedTrial import MITPerson

# Liskov substitution principle
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year
        
    def speak(self, utterance):
        return MITPerson.speak(self, " Yo Bro, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj,Student)
    
s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')
s5 = TransferStudent('Robert deNiro')

'''
studentList = [s1, s2, s3, s4, s5]
for e in studentList:
    print(e)

print(isStudent(s1))
'''

#print(s1)
#print(s1.getClass())
#print(isStudent(s1))
#print(s1.speak('where is the quiz?'))
#
#print(s2.speak('I have no clue!'))
