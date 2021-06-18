#!/usr/bin/python3
import shutil
from shutil import copyfile
import docker
import os
import subprocess
from cMakeAuto import genCMake

def run(codeDir, inputDir, outputDir, time):
    populateFiles(codeDir, inputDir) # fill the directory to be mounted to the docker container

    # create docker container from image, mount volume, and specify bash script to be run on startup
    client = docker.from_env()
    container = client.containers.run("aflplusplus/aflandcmake", "/mnt/bashScripts/aflAuto.sh /mnt/code /mnt/inputs /mnt/output " + str(time) , volumes={os.getcwd() + "/copyIn": {'bind':'/mnt', 'mode': 'rw'}}, detach=True, tty=True, name="workingContainer")
    container.start() # start container object created above
    print(container.name)
    container.stop() # stop container object
    container.remove() # remove container object

    deletefiles(os.getcwd() + "/copyIn/code/", os.getcwd() + "/copyIn/inputs/", outputDir) # clean copyIn directories

    print("Script Complete")

def populateFiles(codeDir, inputDir):
    copyfiles(codeDir, inputDir, os.getcwd() + "/copyIn/code/", os.getcwd() + "/copyIn/inputs/")
    genCMake(os.getcwd() + "/copyIn/code/") # create CMake file in the code directory
    return

def copyfiles(codeDir, inputDir, codeToDir, inputToDir):
    # name of all the files in directories
    listcode = os.listdir(codeDir) 
    listinputs = os.listdir(inputDir)
    
    # copy files to directories
    for code in listcode:
        if (code.endswith('.c') or code.endswith('.h')): # only copy over code files
            shutil.copy(codeDir + "/" + code, codeToDir) 
    for inputs in listinputs:
        shutil.copy(inputDir + "/" + inputs, inputToDir)

    # creating output directory(if needed)
    # os.mkdir(os.path.join(os.getcwd() + "/test/","outputs"))

def deletefiles(codeToDir, inputToDir, outputDir):
    # name of all the files in directories
    listcodeTo = os.listdir(codeToDir)
    listinputsTo = os.listdir(inputToDir)
    # functionality not available yet
    # listoutputs = os.listdir(outputDir)

    # delete all the files in directories
    for i in listcodeTo:
        os.remove(codeToDir + i)

    for j in listinputsTo:
        os.remove(inputToDir + j)

    # must manually delete
    # for k in listoutputs:
        # os.remove(outputDir + k)
    
    # delete output directory(if needed)
    # os.rmdir(os.getcwd() + "/test/outputs/")

if __name__ == "__main__":
    run("/home/myers395/git/pas_backend/afl/testCaseGeneration/test/code", "/home/myers395/git/pas_backend/afl/testCaseGeneration/test/inputs", "~/git/pas_backend/afl/testCaseGeneration/test/outputs", 10)
