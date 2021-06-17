#!/usr/bin/python3
import shutil
from shutil import copyfile
#import docker
import os
import subprocess
import tarfile
from io import BytesIO

def run(codeDir, inputDir, outputDir, time):
    populateFiles(codeDir, inputDir)
    #client = docker.from_env()
    #container = client.containers.run("aflplusplus/aflandcmake", "/mnt/bashScripts/aflAuto.sh /mnt/code /mnt/inputs /mnt/output 10" , volumes={os.getcwd() + "/copyIn": {'bind':'/mnt', 'mode': 'rw'}}, detach=True, tty=True, name="workingContainer")
    #container.start()
    #print(container.name)
    #container.exec_run
    #container.stop()
    deletefiles(os.getcwd() + "/copyIn/code/", os.getcwd() + "/copyIn/inputs/", outputDir)
    #container.remove()

    print("Script Complete")

def populateFiles(codeDir, inputDir):
    copyfiles(codeDir, inputDir, os.getcwd() + "/copyIn/code/", os.getcwd() + "/copyIn/inputs/")
    genCMake(os.getcwd() + "/copyIn/code/")
    return

<<<<<<< HEAD

def copyfiles(codeDir, inputDir, codeToDir, inputToDir):
    # name of all the files in directories
    listcode = os.listdir(codeDir) 
    listinputs = os.listdir(inputDir)
    
    # copy files to directories
    for code in listcode:
        go = shutil.copy(codeDir + code, codeToDir) 
    for inputs in listinputs:
        go2 = shutil.copy(inputDir + inputs, inputToDir)

    # creating output directory(if needed)
    # os.mkdir(os.path.join(os.getcwd() + "/test/","outputs"))

def deletefiles(codeToDir, inputToDir, outputDir):
    # name of all the files in directories
    listcodeTo = os.listdir(codeToDir)
    listinputsTo = os.listdir(inputToDir)
    listoutputs = os.listdir(outputDir)

    # delete all the files in directories
    for i in listcodeTo:
        os.remove(codeToDir + i)

    for j in listinputsTo:
        os.remove(inputToDir + j)

    for k in listoutputs:
        os.remove(outputDir + k)
    
    # delete output directory(if needed)
    # os.rmdir(os.getcwd() + "/test/outputs/")

def genCMake(dir_path):
=======
def genCMake(dir_path, instrument):
>>>>>>> 3cba03514ab264efed84a077571abe954755daba
    #@author: leila_i3viefa

    #dir_path = os.path.dirname(os.path.realpath('C:/afl/code SAMPLE')) #creates variable of the folder to search
    mainfile = open(dir_path + "/CMakeLists.txt",'w') #creates text file

    #list of most of the content for the text file since only the last line of the file changes
    lines = ['cmake_minimum_required(VERSION 3.16)\n', '\n', 'project(binary)\n', '\n', 'set(AFL_FUZZER_DIR "" CACHE STRING "AFL fuzzer binary directory")\n', 'if(AFL_FUZZER_DIR)\n', '    set(CMAKE_C_COMPILER "${AFL_FUZZER_DIR}/afl-clang-lto")\n', 'else()\n', '    set(CMAKE_C_COMPILER afl-clang-lto)\n', 'endif()\n', '\n']
    lineItr = 0;
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

if __name__ == "__main__":
    run("~/git/pas_backend/afl/testCaseGeneration/test/code", "~/git/pas_backend/afl/testCaseGeneration/test/inputs", "~/git/pas_backend/afl/testCaseGeneration/test/outputs", 10)
