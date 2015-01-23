#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Use functools to alter function be decorated
'''

from functools import wraps


def tags(tag_name):
    def tags_deforator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            return '<{0}>{1}</{0}>'.format(tag_name, func(*args, **kwargs))
        return func_wrapper
    return tags_deforator


@tags('p')
def get_text(name):
    '''return text with greeting'''
    return 'Hello {}'.format(name)

print get_text('Guesslin')
print get_text.__name__
print get_text.__doc__
print get_text.__module__
