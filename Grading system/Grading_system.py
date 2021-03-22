# input: a string which is student file pass
# output: a tuple that has <grade, a list about feedback(each element is a string)>

import os
from os import path
from distutils.ccompiler import new_compiler

def grade_a_file_fun(inputfilepass):
    from diff import diff
    # inputfilepass = '/home/tony/research/test.c'    # student submission path in database
    
    # Compileable
    compile_bool = compileable_fun(inputfilepass)
    
    if (compile_bool == 0):  # If the input is not compile able, final grade = 0
        list_final = []
        list_final.append = 'Your code is not compile able, please check gcc errors.'
        grade_final = 0
        return grade_final, list_final

    # Diff
    hwNum = 1  # homework number, need from database
    subPath = '/Users/liang/PycharmProjects/pythonProject/research/diffs/'  # this is for testing, need from database
    diff(hwNum, subPath)  # homework number, path of files need diff

    # Check memory

    # Store final grade
        # front end will deal with storing final grade

    # clean the work space

    return grade_final

# Input: student's file pass
# Output: 0 if not compile able, 1 if compile able.
def compileable_fun(inputfilepass):
    # inputfilepass = '/home/tony/research/test.c'    # student submission path in database
    
    compiler = new_compiler()
    try:
        compiler.compile([inputfilepass])
        compiler.link_executable(['test.o'], 'test')
        #print("True1")
        return 1
    except:
        #print("False1")
        return 0
