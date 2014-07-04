#!/usr/bin/python
#filename: stringextension.py
#functions
#1. trim_enter(line)

# FUNCTION
def trim_enter(line): 
    '''Trim the enter char '\n' at the end of read line''' 
    # null line 
    if not line:
        return line 
    
    # trim the last enter char 
    elif(line[-1] == '\n'):
        return line[:-1] 
    
    # do nothing
    else:
        return line


# FUNCTION


# MAIN FUNCTION 
if __name__ == '__main__':
    words = ['a', 'b', 'c']
    print ' ### '.join(words)
