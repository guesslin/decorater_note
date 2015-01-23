#!/usr/bin/env python
# -*- coding: utf-8 -*-


def greet(name):
    def get_message():
        return "Hello "
    result = get_message()+name

    return result

print greet('Guesslin')
