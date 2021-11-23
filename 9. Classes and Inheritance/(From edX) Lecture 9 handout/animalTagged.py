# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:14:45 2016

@author: ericgrimson
"""
from icecream import ic

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)


class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                       and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite




'''
peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
cotton.set_name('Cottontail')
mopsy = peter + hopsy
print(mopsy == cotton)
'''

rabbit1 = Rabbit(2)
rabbit1.set_name("John")
rabbit2 = Rabbit(3)
rabbit2.set_name("Jill")
rabbit3 = rabbit1 + rabbit2
ic(rabbit3.get_parent1())
ic(rabbit3.get_parent2())
print(rabbit3.get_parent1())
print(rabbit3.get_parent2())

rabbit4 = rabbit2 + rabbit1
print(rabbit4 == rabbit3)
rabbit5 = rabbit1 + rabbit2
print(rabbit3 == rabbit5)
rabbit6 = rabbit3 + rabbit5
print(rabbit3 == rabbit6)





