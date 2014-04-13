#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Test runner. Run all tests in testsuite package
"""
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('.')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)