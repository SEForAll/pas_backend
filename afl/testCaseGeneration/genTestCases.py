from shutil import copyfile
import docker
import os
import subprocess
import tarfile
from io import BytesIO

def run(codeDir, inputDir, outputDir, time):
    populateFiles(codeDir, inputDir)
    client = docker.from_env()
    container = client.containers.run("aflplusplus/aflandcmake", "/mnt/bashScripts/aflAuto.sh /mnt/code /mnt/inputs /mnt/output 10" , volumes={os.getcwd() + "/copyIn": {'bind':'/mnt', 'mode': 'rw'}}, detach=True, tty=True, name="workingContainer")
    container.start()
    print(container.name)
    #container.exec_run
    container.stop()
    container.remove()

    print("Script Complete")

def populateFiles(codeDir, inputDir):
    genCMake(os.getcwd() + "/copyIn/code")
    return

def genCMake(dir_path):
    #@author: leila_i3viefa

    #dir_path = os.path.dirname(os.path.realpath('C:/afl/code SAMPLE')) #creates variable of the folder to search
    mainfile = open(dir_path + "/CMakeLists.txt",'w') #creates text file

    #list of most of the content for the text file since only the last line of the file changes
    lines = ['cmake_minimum_required(VERSION 3.16)\n', '\n', 'project(binary)\n', '\n', 'set(AFL_FUZZER_DIR "" CACHE STRING "AFL fuzzer binary directory")\n', 'if(AFL_FUZZER_DIR)\n', '    set(CMAKE_C_COMPILER "${AFL_FUZZER_DIR}/afl-clang-lto")\n', 'else()\n', '    set(CMAKE_C_COMPILER afl-clang-lto)\n', 'endif()\n', '\n']

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

if __name__ == "__main__":
    run("~/git/pas_backend/afl/testCaseGeneration/test/code", "~/git/pas_backend/afl/testCaseGeneration/test/inputs", "~/git/pas_backend/afl/testCaseGeneration/test/outputs", 10)
