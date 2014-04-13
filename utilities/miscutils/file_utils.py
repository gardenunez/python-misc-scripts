#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
File and directory utilities
'''
import os


def remove_dir(root_dir, dir_name="", recursive=False, verbose=False):
    """
    Remove all dir_name directories in root_dir
    """
    for root, dirs, files in os.walk(root_dir):
        if dir_name in dirs:
            rmdir_recursive(os.path.join(root, dir_name))


def rmdir_recursive(root, exclude=[], verbose=False):
    """
    Remove a directory and sub-directories recursively.
    """
    for name in os.listdir(root):
        if name in exclude:
            continue
        full_name = os.path.join(root, name)
        # on Windows, if we don't have write permission we can't remove
        # the file/directory, so we turn that on
        if not os.access(full_name, os.W_OK):
            os.chmod(full_name, 0600)
        if os.path.isdir(full_name):
            rmdir_recursive(full_name)
        else:
            os.remove(full_name)
            if verbose:
                print '[DONE] remove %s'%full_name
    
    os.rmdir(dir)
    if verbose:
        print '[DONE] remove %s'%dir

def remove_files(dirs, exclude=[]):
    '''
    Remove all files from directory recursively. 
    '''
    for d in dirs:
        for root, dirs, files in os.walk(d):
            for name in files:
                if name not in exclude:
                    os.remove(os.path.join(root, name))

def rename_files(dirs, old, new, recursive=False, verbose=False):
    '''
    Rename all the filenames in directories 
    witch has occurrences of substring old 
    by new.
    '''
    if not check_dirs(dirs):
        raise IOError("cannot find directory")
    files_to_rename = []
    for path in dirs:
        names = get_files(path, old, recursive)
        files_to_rename.extend(names)
    for name,root in files_to_rename:
        if os.path.isfile(os.path.join(root,name)):
            newname = name.replace(old, new)
            if name != newname:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, newname)
                try:
                    os.rename(old_path,new_path)
                except:
                    print "[ERROR] Error renaming %s by %s"%\
                    (old_path, new_path)
            if verbose:
                print "[DONE] Renamed  %s by %s"%\
                (old_path, new_path)


def get_files(root_dir, substr="", recursive=False):
    """ get all files from directory. """
    result = []
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if name.find(substr) >= 0:
                result.append((name, root))
        if not recursive:
            break
    return result


def check_dirs(dirs):
    '''
    Check if directories are valid.
    '''
    for d in dirs:
        if not os.path.isdir(d):
            return False
    return True
