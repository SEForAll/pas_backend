import os
def genCMake(dir_path, instrument):
    #@author: leila_i3viefa

    #dir_path = os.path.dirname(os.path.realpath('C:/afl/code SAMPLE')) #creates variable of the folder to search
    mainfile = open(dir_path + "/CMakeLists.txt",'w') #creates text file

    #list of most of the content for the text file since only the last line of the file changes
    lines = ['cmake_minimum_required(VERSION 3.16)\n', '\n', 'project(binary)\n', '\n', 'set(AFL_FUZZER_DIR "" CACHE STRING "AFL fuzzer binary directory")\n', 'if(AFL_FUZZER_DIR)\n', '    set(CMAKE_C_COMPILER "${AFL_FUZZER_DIR}/afl-clang-lto")\n', 'else()\n', '    set(CMAKE_C_COMPILER afl-clang-lto)\n', 'endif()\n', '\n']
    lineItr = 0
    for element in lines:
        #writes the lines list to the text file
        if(instrument == True and element < 5) or element > 4):  
            mainfile.write(element)
        lineItr = lineItr + 1

    lineLast = "add_executable(${PROJECT_NAME}" #first part of the last line of text file

    for root,dirs,files in os.walk(dir_path): 
        for file in files:
            if file.endswith('.c'):
                #singles out the files with .c ending
                lineLast = lineLast + " " + str(file) #adds the file name to the string of the last line

    lineLast = lineLast + ")"

    mainfile.write(lineLast) #adds the last line to the text file
    mainfile.close() #closes the text file
