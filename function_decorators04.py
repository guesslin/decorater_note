#!/usr/bin/env python
# -*- coding: utf-8 -*-


def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message

greet = compose_greet_func("Guesslin")
print greet()
