#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Python modules utility
"""


def get_mod_names(module_name):
    """
    Get the names of the functions of the module
    TODO: include fromlist argument ( look at fromlist arg in __import__)
    """
    try:
        module = __import__(module_name)
    except ImportError as ie:
        raise ie
    names = [a for a in dir(module) if callable(getattr(module, a))]
    return names

def call_mod_function(module_name, callable_function):
    """
    call function of the module
    """
    try:
        module = __import__(module_name)
    except ImportError as ie:
        raise ie
    try:
        function = getattr(module, callable_function)
        if callable(function):
            return function()
    except AttributeError as ae:
        raise ae

