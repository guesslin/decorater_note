#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Passing arguments to decorators'''


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(*args, **kwargs):
            return '<{0}>{1}</{0}>'.format(tag_name, func(*args, **kwargs))
        return func_wrapper
    return tags_decorator


class Person(object):
    def __init__(self):
        self.name = "Guesslin"
        self.last = "Lin"

    @tags('div')
    @tags('p')
    @tags('strong')
    def get_fullname(self):
        return self.name + ' ' + self.last

my_person = Person()

print my_person.get_fullname()
