#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from os.path import join

#TODO:re-use rmdir from file_utils, verbose arg
#TODO:add logging tools, add tests

def remove_cvs_dirs(path,dir_name = 'CVS', recursive=False, verbose = 1):
    """
    Remove all CVS directories
    """
    for root, dirs, files in os.walk(path):
        if dir_name in dirs:
            rmdir_recursive(os.path.join(root, dir_name))

def rmdir_recursive(dir, verbose = 1):
    """
    Remove a directory, and all its contents if it is not already empty.
    """
    for name in os.listdir(dir):
        full_name = os.path.join(dir, name)
        # on Windows, if we don't have write permission we can't remove
        # the file/directory either, so turn that on
        if not os.access(full_name, os.W_OK):
            os.chmod(full_name, 0600)
        if os.path.isdir(full_name):
            rmdir_recursive(full_name)
        else:
            if verbose:
                print 'removing ', full_name
            os.remove(full_name)
    os.rmdir(dir)
    
#if __name__ == '__main__':
#    remove_cvs_dirs(sys.argv[1], sys.argv[2], verbose = True)
