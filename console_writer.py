#this is the branch from test
#!/usr/bin/pyth
#filename: consolewriter.py
#Functions:
#1. WritePercentage(finished_count, total_count)

# IMPORT
import os
import os.path
import sys
import string
import time

#CLASS
class ConsoleWriter(object):
    """Use for print the content for the console"""
# static memebers
#only use for print percentage
    _percentage_started = False
    _percentage_next_step = 0
    _percentage_last_finished = 0
    _percentage_accuracy = 0.001
    _percentage_over_finished = False

    # FUNCTION
    @staticmethod
    def WritePercentage(finished_count, total_count):
        try:
            # valid print argument
            if finished_count >= 0 and finished_count <= total_count:
                
                # new print request
                if finished_count < ConsoleWriter._percentage_last_finished:
                    ConsoleWriter._percentage_started = False
                    ConsoleWriter.percentage_last_finished = 0
                    ConsoleWriter._percentage_next_step = 0
                
                # need to print
                if (not ConsoleWriter._percentage_started
                    or finished_count >= ConsoleWriter._percentage_next_step
                    or finished_count == total_count):
                    
                    # need to print an empty line at the very beginning 
                    if not ConsoleWriter._percentage_started:
                        print
                    
                    #start to print percentage
                    ConsoleWriter._percentage_started = True
                    percentage = finished_count * 100 / total_count
                    print '\r' + round(percentage, 1).__str__() + '%',
                    sys.stdout.flush()

                    #set next print step
                    step = long(
                        total_count 
                        * ConsoleWriter._percentage_accuracy)
                    if step <= 0:
                        step = 1
                    while ConsoleWriter._percentage_next_step <= finished_count:
                        ConsoleWriter._percentage_next_step += step

                #end print region
                ConsoleWriter._percentage_last_finished = finished_count
                ConsoleWriter._percentage_over_finished = False

            #over finished
            elif not ConsoleWriter._percentage_over_finished:
                print 'The process is over finished the total count of', total_count
        except Exception as e:
            print e	


# ENUM CLASS
class ConsoleColors:
    '''Different colors use for console printing'''
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'


# FUNCTION
def print_with_color(content, color=ConsoleColors.YELLOW):
    '''print the content with color'''
    try:
        # error: input is not a pre-defined color
        if (color != ConsoleColors.PURPLE
            and color != ConsoleColors.BLUE
            and color != ConsoleColors.GREEN
            and color != ConsoleColors.YELLOW
            and color != ConsoleColors.RED
            and color != ConsoleColors.DEFAULT):
            raise Exception('The input color %s is not\
                    pre-defined color in ConsoleColors')
        
        # print
        print(
            color + 
            str(content) +
            ConsoleColors.DEFAULT)
    except Exception as e:
        print e


#MAIN FUNCTION			
if __name__ == '__main__':
    file = '/home/ustcwhc/Programs/python/poem.txt'
    print_with_color(
            [1, 2],
            ConsoleColors.GREEN)
