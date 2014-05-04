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
    def setUp(self):
        """
        Setup test class
        """
        self.valid_dirs = ['/bin', '/boot', '/home', '/tmp']
        self.invalid_dir = '/unexistent'

    def test_check_dirs_true(self):
        result = file_utils.check_dirs(self.valid_dirs)
        self.assertTrue(result)

    def test_check_dirs_false(self):
        result = file_utils.check_dirs([self.valid_dirs[0], self.invalid_dir])
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
