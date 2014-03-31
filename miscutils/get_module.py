#!/usr/bin/python
"""
Utility to get names and/or call features of a python modules
"""
import sys
import argparse


def get_args():
    '''
    '''
    parser = argparse.ArgumentParser(prog = "get_module", 
                                     description = "get info and run module's features",
                                     epilog = "gardenunez")
    parser.add_argument("-m", "--module" ,
                        help = "module name", required = True)
    parser.add_argument("-a", "--attr", help = "attribute to be called")
    args = parser.parse_args()
    return args

def get_module_names(module_name):
    """
    Get the names of the functions of the module
    """
    try:
        module = __import__(module_name)
    except ImportError as ie:
        print ie
        sys.exit(1)
    for name in dir(module):
        obj = getattr(module, name)
        if callable(obj):
            print obj.__name__

def call_module_function(module_name, function_name):
    """
    call function of the module
    """
    try:
        module = __import__(module_name)
    except ImportError as ie:
        print ie
        sys.exit(1)
    for name in dir(module):
        obj = getattr(module, name)
        if callable(obj) and obj.__name__ == function_name:
            return obj()



def main():
    """
    Entry point function
    """
    args = get_args()
    
    if args.attr:
        call_module_function(args.module, args.attr)
    else:
        get_module_names(args.module)
    




if __name__ == "__main__":
    main()
