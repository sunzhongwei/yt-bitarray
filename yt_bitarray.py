#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.1"
__author__ = "Zhongwei Sun (zhongwei.sun2008@gmail.com)"

# ----------------------------------------
# Just say "Hello world!".
# ----------------------------------------

# build-in, 3rd party and my modules

class YTBitArray(object):
    def __init__(self, available_choices):
        available_choices.reverse()
        self.available_choices = available_choices
        self.choices_count = len(available_choices)

    def convert_choices_to_int(self, choices):
        value = 0
        for choice in choices:
            try:
                index = self.available_choices.index(choice)
            except ValueError:
                pass
            value = value | (1 << index)

        return value

    def convert_int_to_choices(self, value):
        choices = []
        binary_string = bin(value)[2:].zfill(self.choices_count)
        for index, selected in enumerate(binary_string):
            if selected == "1":
                choices.append(
                        self.available_choices[self.choices_count - index - 1])

        return choices

