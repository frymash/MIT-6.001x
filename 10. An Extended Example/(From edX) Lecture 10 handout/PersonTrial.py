# -*- coding: utf-8 -*-
"""
Created on Wed May 18 07:51:28 2016

@author: ericgrimson

From Unit 5 (OOP), Chapter 10, Video 1 - Building a Class
"""

import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName
        
    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    
    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName



    # other methods

    def __str__(self):
        """return self's name"""
        return self.name
        

# example usage

p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')


personList = [p1, p2, p3, p4, p5]

'''
for e in personList:
    print(e)

# Sorting is done here on the basis of lexicographical order where A < a < z.
# Hence, the object.sort() method is reliant on the Person.__lt__ method here.

# Based on Person.__lt__'s definition, Person.__lt__() helps object.sort() sort 
# names by ordering last names alphabetically. If the last name of 2 elements
# are identical, the 2 elements will then be sorted by the alphabetical order
# of their first names.

personList.sort()

print()

for e in personList:
    print(e)
'''
