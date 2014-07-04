#!/usr/bin/python
#Filename FileReader.py
#Functions:
#1. read_row(file_path, row_index=0):
#2. read_rows(file_path, row_index, length=-1):
#3. get_line_count(file_path):
#4. read_column(file_path, column_index, splitor='\t'):
#5. read_to_dic(file_path, splitor='\t'):
#6. read_to_array_list(file_path, splitor='\t')
# IMPORT
import string_extension


# FUNCTION
def read_row(file_path, row_index=0):
    '''Read line by specified line index'''
    
    # initialize
    sr = open(file_path)

    # read to the specific line number
    for i in range(0, row_index + 1):
        line = sr.readline()
        
        # there no enough lines
        if not line:
            sr.close()
            return None

    # return
    sr.close()
    return string_extension.trim_enter(line)


# FUNCTION
def read_rows(file_path, row_index, length=-1):
    '''Read lines by specified start index and line count'''
    # error
    if length == 0:
        return None
    # initialize	
    lines = []
    line_count = 1
    sr = open(file_path)
    line = sr.readline()
    end_line_count = row_index + length
    
    # add line
    while (length < 0 or line_count <= end_line_count) and line:
        if line_count > row_index:
            lines.append(string_extension.trim_enter(line))
        
        # read new line
        line = sr.readline()
        line_count += 1

    # return
    sr.close()
    return lines


# FUNCTION
def get_line_count(file_path):
    '''Get the line count of the input file'''
    
    # initialize
    sr = open(file_path)
    line_count = 0
    line = sr.readline()

    # while not end
    while line:
        # add number
        line_count += 1

        # use to avoid the last empty line of the file
        last_is_empty = line == '\n'

        # read new line
        line = sr.readline()

    # -1 to avoid the last empty line
    if last_is_empty:
        line_count -= 1

    # finish
    sr.close()
    return line_count


# FUNCTION
def read_column(file_path, column_index, splitor='\t'):
    '''Read specific column of the input file'''

    # initialize
    sr = open(file_path)
    lines = []
    line = sr.readline()

    # while not end
    try:
        while line:
            # only operate non-empty line
            if line != '\n':
                line_array = string_extension.trim_enter(line).split(splitor)
                if len(line_array) < column_index + 1:
                    raise Exception("There is no %d columns in line %s"% 
                                    (column_index + 1, line))
                # add column
                lines.append(line_array[column_index])

            # read new line
            line = sr.readline()
    except Exception as e:
        print e
    
    # finally
    sr.close()
    return lines


# FUNCTION
def read_to_dic(file_path, splitor='\t'):
    '''Read the file to a dictionary, first column is key, remain is value'''

    # initialize
    sr = open(file_path)
    dic = {}
    line = sr.readline()

    # while not end
    try:
        while line:
            if line != '\n':
                line_array = string_extension.trim_enter(line).split(splitor)

                # error: no enough column
                if len(line_array) < 2:
                    raise Exception(
                            "There is no enough columns in line: " 
                            + line)

                # read to key value and add to dictionary
                key = line_array[0]
                value = line_array[1:]
                if not dic.has_key(key):
                    dic[key] = value
        
            # new line
            line = sr.readline()

    # handle except
    except Exception as e:
         print e

    # finally	
    sr.close()
    return dic



# FUNCTION
def read_to_array_list(file_path, splitor='\t'):
    '''Split each line by splitor into array, and merge these array by list'''
    #initialize
    array_list = []

    #split each line and append to array_list
    with open(file_path) as sr:
        line = sr.readline()
        while line:
            if line != '\n':
                array_list.append(
                        string_extension.trim_enter(line)
                        .split(splitor))
            line = sr.readline()

    return array_list


# MAIN FUNCTION
if __name__ == '__main__':
    file = '/home/ustcwhc/Programs/python/poem.txt'

    for array in read_to_array_list(file):
        print array
