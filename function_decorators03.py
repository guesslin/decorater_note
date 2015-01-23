#!/usr/bin/env python
# -*- coding: utf-8 -*-


def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print greet()
