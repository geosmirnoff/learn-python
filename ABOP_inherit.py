#!/usr/bin/env python
# Filename: ABOP_inherit.py

from abc import *

class SchoolMember(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Создан SchoolMember: {0}'.format(self.name))

    @abstractmethod 
    def tell(self):
        print('Имя: {0} Возраст: {1}'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Создан Teacher: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: {0:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Создан Student: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: {0:d}'.format(self.marks))

t = Teacher('Marywanna', 42, 500000000000)
s = Student('Vovo4ka', 12, 2)

print()

members = [t, s]

for member in members:
    member.tell()
