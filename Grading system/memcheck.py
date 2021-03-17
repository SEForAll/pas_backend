import re
import os

# file --> a file that has all the valgrind information on it (not verbose)
# returns how many bytes are in use and in how many blocks at the end of the program
def memcheck(makefile_dir, path_to_test_case, name_of_test_case):
    os.chdir("../../../../../../../..")
    os.chdir(path_to_test_case)
    with open(name_of_test_case) as f:
        testcase = f.read()

    os.chdir("../../../../../../../..")
    os.chdir(makefile_dir)

    with open("makefile", 'r') as f:
        text = f.read()
        ex = re.compile(r'-o (\w+)')
        match = ex.search(text)
        if match is not None:
            executable = match.group(1)
        else:
            return -1, -1 # happens when the name of the executable cannot be found from the makefile

    os.system("make")  # compiles the code according to the makefile

    testfile = "testcase.txt"
    with open(testfile, 'w') as f:
        f.write(testcase)

    tempfile = "tempfile.txt"  # the path to the tempfile
    os.system("valgrind ./" + executable + " " + testfile + " > " + tempfile + " 2>&1")
    # previous statement executes valgrind on the code and writes the output to the tempfile

    p = re.compile(r'in use at exit: (\d+) bytes in (\d+) blocks')

    with open(tempfile, 'r') as f:
        text = f.read()
        match = p.search(text)
        if match is None:
            return -2, -2 # return this if the valgrind is not called properly (might happen bc i wrote this on mac)
        bytesInUse = int(match.group(1))
        blocks = int(match.group(2))

    os.remove(tempfile)
    os.remove(testfile)

    return bytesInUse, blocks


### EXAMPLE CODE THAT WORKS ON ALEX'S COMPUTER

makefile_dir = "Users/alexgieson/Desktop/hw14"  # the directory of the makefile starting at the root
path_to_test_case = "Users/alexgieson/Desktop/hw14/inputs"  # the path to the test case from root
testcase = "input1.txt"

bytes, blocks = memcheck(makefile_dir, path_to_test_case, testcase) # opens the file and sends it to the memcheck funciton to get integer values

if bytes >= 0:
    print(f'you have {bytes} bytes of memory leak')
elif bytes == -1:
    print('the name of the executable could not be found')
elif bytes == -2:
    print('valgrind did not output to the correct file')