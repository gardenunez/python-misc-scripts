#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Tests for file utils
'''
import unittest

import utilities.miscutils.file_utils as file_utils


class TestFileUtils(unittest.TestCase):
    """
    File Utils test class
    """

    def test_check_dirs_true(self):
        result = file_utils.check_dirs(['/bin', '/boot', '/home', '/tmp'])
        self.assertTrue(result)

    def test_check_dirs_false(self):
        result = file_utils.check_dirs(['/bin', '/unexistent', '/home'])
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()