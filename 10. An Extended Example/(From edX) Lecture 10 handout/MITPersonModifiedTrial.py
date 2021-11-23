# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:10:59 2016

@author: ericgrimson

From Unit 5 (OOP), Chapter 10, Video 2 - Visualizing the Hierarchy

While reading through this file, it'd be a good idea to have PersonTrial.py 
open as well for easier reference to the Person class definition.
"""

from PersonTrial import Person
import datetime

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
        
    def speak(self, utterance):
        return (self.name + " says: " + utterance)

        

# example usage

m3 = MITPerson('Mark Zuckerberg')
m3.setBirthday(5,14,84)
m1 = MITPerson('Bill Gates')
m1.setBirthday(10,28,55)
m2 = MITPerson('Drew Houston')
m2.setBirthday(3,4,83)
m4 = Person('Travis Kalanik')
m5 = Person('Steve Wozniak')

MITPersonList = [m1, m2, m3]

'''
# Prints in the order of MITPersonList: m1, m2, m3
print("Unsorted MITPersonList:")
for e in MITPersonList:
    print(e, e.getIdNum())

# Sorts by .nextIdNum
MITPersonList.sort()

print()

print("Sorted MITPersonList: ")
for e in MITPersonList:
    print(e, e.getIdNum())
'''

# Comparing Person and MITPerson objects (7:10 - 10:50 in the video)
# Here, m4 is a Person object and m1 is an MITPerson object

# print(m4 < m1) 
# For the statement above, m4 < m1 -> m4.__lt__(m1) -> Person.__lt__(m1) -> False

# print(m1 < m4) 
# For the statement above, MITPerson.__lt__() shadows Person.__lt__() 
# since MITPerson is a subclass of person and MITPerson's methods thus take precedence.
# m1 < m4 -> m1.__lt__(m4) -> MITPerson.__lt__(m4) 
# -> error since Person doesn't have the idNum attr like MITPerson
