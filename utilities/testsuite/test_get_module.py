#!/usr/bin/python
"""
Tests for get_module
"""
import unittest

from utilities.miscutils.module_utils import get_mod_names, call_mod_function


class TestModuleUtils(unittest.TestCase):
    """
    Unit test for module_utils features
    """
    def setUp(self):
        """
        Setup tests needs.
        """
        pass
    
    def test_get_mod_names_invalid_name(self):
        """
        """
        self.assertRaises(ImportError, get_mod_names, "mod_name")
    
    def test_get_mod_names_valid(self):
        """
        """
        names = get_mod_names("os")
        self.assertIsNotNone(names, "None result")
        self.assertIsInstance(names, list, "Is not a list")
        self.assertGreater(len(names), 0, "List has not elements")
    
    def test_call_mod_function_invalid_mod_name(self):
        """
        """
        self.assertRaises(ImportError, call_mod_function, "mod_name", "function_name")
    
    def test_call_mod_function_invalid_function_name(self):
        """
        """
        self.assertRaises(AttributeError, call_mod_function, "os", "function_name")
    
    def test_call_mod_function_valid(self):
        """
        """
        res = call_mod_function("sys", "getdefaultencoding")
        self.assertIsNotNone(res, "None result")
        self.assertIsInstance(res, str, "Result should be string")
     
if __name__ == "__main__":
    unittest.main()
