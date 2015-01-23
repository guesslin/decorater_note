#!/usr/bin/env python
# -*- coding: utf-8 -*-


def p_decorate(func):
    def func_wrapper(name):
        return '<p>{0}</p>'.format(func(name))
    return func_wrapper


@p_decorate
def get_text(name):
    return 'Hi there, {0}!!'.format(name)

print get_text('Guesslin')
