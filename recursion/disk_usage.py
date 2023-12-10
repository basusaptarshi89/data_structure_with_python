# recursively calculate the size of folder, sub-folders and files
# used Python os module
# https://docs.python.org/3/library/os.path.html#module-os.path
#
# os.path.getsize(path) --> Return the size, in bytes, of path. Raise OSError if the file does not exist or is inaccessible.
# os.path.isdir(path)   --> Return True if path is an existing directory. This follows symbolic links, so both islink() and isdir() can be true for the same path.
# os.listdir(path='.')  --> Return a list containing the names of the entries in the directory given by path. 
#                           The list is in arbitrary order, and does not include the special entries '.' and '..' even if they are present in the directory. 
#                           If a file is removed from or added to the directory during the call of this function, whether a name for that file be included is unspecified.
# os.path.join  --> 

import os

def tree(path):
    print(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            fully_qualified_child_path = os.path.join(path, filename)
            tree(fully_qualified_child_path)

# tree(r"C:\Users\basus\Git\data_structure_with_python")

print('#' * 75)

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            fully_qualified_child_path = os.path.join(path, filename)            
            total += disk_usage(fully_qualified_child_path)
    print(str(total).ljust(15), path)
    return total

disk_usage(r"C:\Users\basus\Git\udemy_spark_tutorial")