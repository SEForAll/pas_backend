import subprocess
import os

def testInputs(inRootPath, outPath, program):
    fileNum = 1
    while(os.path.isfile(str(inRootPath + str(fileNum)))):
        with open(str(inRootPath + str(fileNum))) as f:
            programData = subprocess.Popen([str('./' + program)], stdout=subprocess.PIPE, stdin=f).communicate()
            output = programData[0]
            outF = open(str(outPath + str(fileNum)), "w")
            outF.write(bytes.decode(output))
        fileNum = fileNum + 1
    dirIn = os.path.dirname(os.path.realpath(inRootPath))
    dirOut = os.path.dirname(os.path.realpath(outPath))
    return [dirIn, dirOut]


    
