# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:54:37 2021

@author: leila_i3viefa
"""

import os
dir_path = os.path.dirname(os.path.realpath('C:/afl/code SAMPLE')) #creates variable of the folder to search
mainfile = open("CMakeLists.txt",'w') #creates text file

#list of most of the content for the text file since only the last line of the file changes
lines = ['cmake_minimum_required(VERSION 3.16)\n', '\n', 'project(broke)\n', '\n', 'set(AFL_FUZZER_DIR "" CACHE STRING "AFL fuzzer binary directory")\n', 'if(AFL_FUZZER_DIR)\n', '    set(CMAKE_C_COMPILER "${AFL_FUZZER_DIR}/afl-clang-lto")\n', 'else()\n', '    set(CMAKE_C_COMPILER afl-clang-lto)\n', 'endif()\n', '\n']

for element in lines:
    #writes the lines list to the text file
    mainfile.write(element)

lineLast = "add_executable(${PROJECT_NAME}" #first part of the last line of text file

for root,dirs,files in os.walk(dir_path): 
    for file in files:
        if file.endswith('.c'):
            #singles out the files with .c ending
            lineLast = lineLast + " " + str(file) #adds the file name to the string of the last line
           
lineLast = lineLast + ")"

mainfile.write(lineLast) #adds the last line to the text file
mainfile.close() #closes the text file