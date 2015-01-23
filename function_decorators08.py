#!/usr/bin/env python
# -*- coding: utf-8 -*-


def p_decorate(func):
    def func_wrapper(self):
        return '<p>{0}</p>'.format(func(self))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "Guesslin"
        self.last = "Lin"

    @p_decorate
    def get_fullname(self):
        return self.name + ' ' + self.last

my_person = Person()

print my_person.get_fullname()
