import os
from os import path
from distutils.ccompiler import new_compiler

def compileable_fun(inputfilename):
    inputfilename = '/home/tony/research/test.c'    # student submission path in database

    compiler = new_compiler()
    try:
        compiler.compile([inputfilename])
        compiler.link_executable(['test.o'], 'test')
        print("True1")
        return 1
    except:
        print("False1")
        return 0
