#!/usr/bin/pyth
# filename: consolewriter.py
# Functions:
# 1. WritePercentage(finished_count, total_count)
# 2. write_with_style(content, *console_styles)
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
    def write_percentage(finished_count, total_count):
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
class ConsoleStyles:
    '''Different colors use for console printing'''
    DEFAULT = 'DEFAULT'
    BOLD = 'BOLD'
    UNDERLINE = 'UNDERLINE'
    FLICKER = 'FLICKER'
    INVERSE = 'INVERSE'
    HIDE = 'HIDE'
    BACK_BLACK = 'BACK_BLACK'
    BACK_DEEPRED = 'BACK_DEEPRED'
    BACK_GREEN = 'BACK_GREEN'
    BACK_YELLOW = 'BACK_YELLOW'
    BACK_BLUE = 'BACK_BLUE'
    BACK_PURPLE = 'BACK_PURPLE'
    BACK_DEEPGREEN = 'BACK_DEEPGREEN'
    BACK_WHITE = 'BACK_WHITE'
    FORE_PURPLE = 'FORE_PURPLE'
    FORE_BLUE = 'FORE_BLUE'
    FORE_GREEN = 'FORE_GREEN'
    FORE_YELLOW = 'FORE_YELLOW'
    FORE_RED = 'FORE_RED'

    _item_dic = {
        'DEFAULT' : '0',
        'BOLD' : '1',
        'UNDERLINE' : '4',
        'FLICKER' : '5',
        'INVERSE' : '7',
        'HIDE' : '8',
        'BACK_BLACK' : '40',
        'BACK_DEEPRED' : '41',
        'BACK_GREEN' :  '42',
        'BACK_YELLOW' : '43',
        'BACK_BLUE' : '44',
        'BACK_PURPLE' : '45',
        'BACK_DEEPGREEN' : '46',
        'BACK_WHITE' : '47',
        'FORE_PURPLE' : '95',
        'FORE_BLUE' : '94',
        'FORE_GREEN' : '92',
        'FORE_YELLOW' : '93',
        'FORE_RED' : '91'
    }

# FUNCTION
def write_with_style(content, *console_styles):
    '''get the console printed string with different style'''
    try:
        # do not contain anything
        if len(console_styles) <= 0:
            return content

        # check the input of each console_style
        ids = []
        for style in console_styles:
            if not ConsoleStyles._item_dic.has_key(style):
                raise Exception('Do not have the ConsoleStyle:%s'% style)
            else:
                ids.append(ConsoleStyles._item_dic[style])
        # merge strings
        # format: '\033[style1;style2;...m' + content + '\033[0m'
        # (style + content + end)
        print '\033[' + ';'.join(ids) + 'm' + content + '\033[0m'

    except Exception as e:
        print e

#MAIN FUNCTION			
if __name__ == '__main__':
    file = '/home/ustcwhc/Programs/python/poem.txt'
    write_with_style('Wu Haocheng loves NIUNIU', ConsoleStyles.BOLD, ConsoleStyles.UNDERLINE, ConsoleStyles.BACK_GREEN, ConsoleStyles.FORE_RED)
