import subprocess
import os
def compareBinaries(expectedFileName, actualFileName):
    numOfSuccess = 0
    numRan = 0
    fileNum = 1
    while(os.path.isfile((expectedFileName + str(fileNum)))):
        biOnePath = str(expectedFileName + str(fileNum))
        biOne = subprocess.run(["cat", biOnePath], capture_output = True)
        expected = str(biOne.stdout)
        if(os.path.isfile((actualFileName + str(fileNum)))):
            biTwoPath = str(actualFileName + str(fileNum))
            biTwo = subprocess.run(["cat", biTwoPath], capture_output = True)
            actual = str(biTwo.stdout)
            if(expected == actual):
                numOfSuccess = numOfSuccess + 1
        numRan= numRan + 1
        fileNum = fileNum + 1
    print(str(numOfSuccess) + " of " + str(numRan) +  " tests passed.")
    print(str(numRan - numOfSuccess) + " of " + str(numRan) + " tests failed.")
    return [numOfSuccess, numRan]
