#!/usr/bin/python
# filename: file_path.py
# functions
# 1. change_extension(file_path, extension)
# 2. add_extension(file_path, extension)
# 3. change_file(file_path, file_name)

# IMPORT
import os.path

# FUNCTION
def change_extension(file_path, extension):
    '''Change the extension of the input file'''
    # error of extension
    if extension.strip() == '':
        return file_path

    # error of file path
    if file_path.strip() == '':
        return ''

    # get file path without extension
    file_without_ext = os.path.splitext(file_path)[0]

    # get valid extension
    valid_ext = extension.strip()
    if(valid_ext[0] != '.'):
        valid_ext = '.' + valid_ext
    
    return file_without_ext + valid_ext

# FUNCTION
def add_extension(file_path, extension):
    '''Add an extension before the original extension'''
    # error of extension
    if extension.strip() == '':
        return file_path

    # error of file path
    if file_path.strip() == '':
        return ''

    # get valid extension
    valid_ext = extension.strip()
    if(valid_ext[0] != '.'):
        valid_ext = '.' + valid_ext

    # insert
    file_and_ext = os.path.splitext(file_path)
    return file_and_ext[0] + valid_ext + file_and_ext[1] 

# FUNCTION
def change_file(file_path, file_name):
    '''Change the file name of the original file'''
    # error of file_name
    if file_name.strip() == '':
        return file_path

    # error of file_path
    if file_path.strip() == '':
        return file_name

    # get valid file name
    valid_file_name = os.path.basename(file_name)

    # get original dir and file name
    dir_and_file = os.path.split(file_path)
    
    # change
    return os.path.join(dir_and_file[0], valid_file_name)


# MAIN FUNCTION
if __name__ == '__main__':
    file = '/home/ustcwhc/Programs/python/poem.txt'
    print change_file(file, '/abcdedadf/gogog.txt') 
