#!/usr/bin/env python
# -*- coding: utf-8 -*-


def greet(name):
    return 'Hello ' + name


def call_func(func):
    other_name = 'guesslin'
    return func(other_name)

print call_func(greet)
