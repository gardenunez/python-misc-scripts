import sys
import argparse

def get_args():
    '''
    '''
    parser = argparse.ArgumentParser(prog = "get_module", 
                                     description = "get info and run module's features",
                                     epilog = "gardenunez")
    subparser = parser.add_subparsers(dest = "action")
    name_parser = subparser.add_parser("names", help = "get function names of the module")
    run_parser = subparser.add_parser("run", help = "run function name of the module")
    
    args = parser.parser_args()
    return args

def get_module_names(module):
    """
    Get the names of the methods of the module
    """
    #module = __import__(sys.argv[1])
    for name in dir(module):
        obj = getattr(module, name)
            if callable(obj):
                print obj.__name__


def main()
    """
    Entry point function
    """
    args = get_args()


if __name__ == "__main__":
    main()
    

#module = __import__(sys.argv[1])
#for name in dir(module):
#   obj = getattr(module, name)
#   if callable(obj):
#      print obj.__name__
