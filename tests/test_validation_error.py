#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of the Kount python sdk project https://github.com/Kount/kount-ris-python-sdk/)
# Copyright (C) 2017 Kount Inc. All Rights Reserved.
"""TestValidationError"""
from __future__ import (
    absolute_import, unicode_literals, division, print_function)
import unittest
from kount.util.validation_error import ValidationError, ValidationErrorType

__author__ = "Yordanka Spahieva"
__version__ = "1.0.0"
__maintainer__ = "Yordanka Spahieva"
__email__ = "yordanka.spahieva@sirma.bg"
__status__ = "Development"


class TestValidationError(unittest.TestCase):
    "TestValidationError"
    def test_max_length(self):
        "test_max_length"
        incorrect = "a"*10
        lengthr = 2
        vale = ValidationError(field=incorrect, length=lengthr)
        with self.assertRaises(ValidationError):
            raise vale
        self.assertEqual(
            str(vale),
            "('LENGTH', 'Field [%s] has length [%s] which is longer "
            "than the maximum of [%s]')" % (incorrect, len(incorrect), lengthr))

    def test_mode(self):
        "test_mode"
        incorrect = "a" * 10
        mode = "q"
        vale = ValidationError(field=incorrect, mode=mode)
        with self.assertRaises(ValidationError):
            raise vale
        self.assertEqual(
            str(vale),
            "('REQUIRED', 'Required field [%s] missing for mode [%s]')" % (
                incorrect, mode.upper()))

    def test_correct_type(self):
        "test_correct_type"
        for correct in ["REGEX_ERR", "REQUIRED_ERR", "LENGTH_ERR"]:
            vale = ValidationErrorType(correct)
            with self.assertRaises(ValidationErrorType):
                raise vale
            self.assertEqual("Expected value of the error type LENGTH, "
                             "REGEX, REQUIRED, found [%s]" % correct, str(vale))

    def test_incorrect_type(self):
        "test_incorrect_type"
        incorrect = "42"
        vale = ValidationErrorType(message=incorrect)
        with self.assertRaises(ValidationErrorType):
            raise vale
        self.assertEqual(
            str(vale),
            "Expected value of the error type LENGTH, REGEX, REQUIRED, "\
            "found [%s]" % incorrect)

    def test_empty_field(self):
        "test_empty_field"
        incorrect = ""
        vale = ValidationErrorType(message=incorrect)
        with self.assertRaises(ValidationErrorType):
            raise vale
        self.assertEqual(
            str(vale),
            "Expected value of the error type LENGTH, REGEX, REQUIRED, "\
            "found [%s]" % incorrect)

    def test_no_field(self):
        "test_no_field"
        incorrect = None
        vale = ValidationErrorType(message=incorrect)
        with self.assertRaises(ValidationErrorType):
            raise vale
        self.assertEqual(
            str(vale),
            "Expected value of the error type LENGTH, REGEX, REQUIRED,"
            " found [%s]" % incorrect)

    def test_none_field(self):
        "test_none_field"
        vale = ValidationErrorType()
        with self.assertRaises(ValidationErrorType):
            raise vale
        self.assertEqual(
            str(vale),
            "Expected value of the error type LENGTH, REGEX, REQUIRED, found []"
            )

    def test_pattern(self):
        "test_pattern"
        field = 'RFCB'
        value = "42"
        pattern = '^[RC]?$'
        vale = ValidationError(field=field, value=value, pattern=pattern)
        with self.assertRaises(ValidationError):
            raise vale
        self.assertEqual(
            str(vale),
            "('REGEX', 'Field [%s] has value [%s] which which does not"
            " match the pattern [%s]')" % (field, value, pattern))


if __name__ == "__main__":
    unittest.main()
