#!/usr/bin/python
"""
Utility to get names and/or call features of a python modules
"""
import argparse

from module_utils import get_mod_names, call_mod_function


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


def main():
    """
    Entry point function
    """
    args = get_args()
    
    if args.attr:
        call_mod_function(args.module, args.attr)
    else:
        names = get_mod_names(args.module)
        for n in names:
            print n
    

if __name__ == "__main__":
    main()
