# -*- coding: utf-8 -*-
from operator import itemgetter


class MyError(Exception):
    def __str__(self):
        return "Error text"


class Parent(object):
    def __init__(self):
        object.__setattr__(self, "i", None)

    def fnc(self, first_value, second_value=None):
        return first_value * second_value * self.i if second_value else first_value * first_value * self.i


class First(Parent):
    def __init__(self):
        super(First, self).__init__()
        object.__setattr__(self, "i", 3)
        object.__setattr__(self, "isSecond", 0)

    @staticmethod
    def isFirst(input_value=None):
        return 1

    def __setattr__(self, *args):
        raise AttributeError


class A(First):
    def fnc(self, first_value, second_value=None):
        if first_value > 6:
            raise MyError
        return first_value * second_value * self.i if second_value else first_value * first_value * self.i


class Second(Parent):
    def __init__(self, i):
        super(Second, self).__init__()
        object.__setattr__(self, "i", i)
        object.__setattr__(self, "isSecond", 1)

    @staticmethod
    def isFirst(input_value=None):
        return 0

    def __setattr__(self, *args):
        raise AttributeError
