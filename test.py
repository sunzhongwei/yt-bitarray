#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------
# DESCRIPTION
# ===========
#
# ----------------------------------------

# build-in, 3rd party and my modules
import unittest
from yt_bitarray import YTBitArray


class TestYTBitArray(unittest.TestCase):
    def setUp(self):
        available_choices = ["apple", "banana", "mongo", "orange", "pear"]
        self.bit_array = YTBitArray(available_choices)

    def tearDown(self):
        pass

    def test_convert_choices_to_int(self):
        selected_choices = ["apple", "orange"]
        value = self.bit_array.convert_choices_to_int(selected_choices)

        expected_value = int("10010", 2)
        self.assertEqual(expected_value, value)

        selected_choices = ["banana", "pear"]
        value = self.bit_array.convert_choices_to_int(selected_choices)

        expected_value = int("01001", 2)
        self.assertEqual(expected_value, value)

    def test_for_fail(self):
        value = int("10010", 2)
        selected_choices = self.bit_array.convert_int_to_choices(value)

        expected_value = ["apple", "orange"]
        for item in expected_value:
            self.assertIn(item, selected_choices)


if '__main__' == __name__:
    unittest.main()

