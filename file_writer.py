#!/usr/bin/python
# filename: file_writer.py
# functions
# 1. print_list(file_path, input_list)
# 2. print_dictionary(file_path, input_dic)

# FUNCTION
def print_list(file_path, input_list):
    '''print each item in the input_list as a line in the file_path'''
    with open(file_path, 'w') as sw:
        for item in input_list:
            sw.write(item.__str__() + '\n')

def print_double_list(file_path, input_double_list, connector='\t'):
    '''print each list in the double list as a line in the file_path
    (connect each item by connector)'''
    with open(file_path, 'w') as sw:
        for item in input_double_list:
            sw.write(connector.join(item.__str__()) + '\n')


# MAIN FUNCTION
if __name__ == '__main__':
    file = '/home/ustcwhc/Programs/python/poem2.txt'
    input_list = [[1,2,3],[4,5.6],[7,8,9]]
    print_double_list(file, input_list)
