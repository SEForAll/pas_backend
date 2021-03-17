import re
import os

# file --> a file that has all the valgrind information on it (not verbose)
# returns how many bytes are in use and in how many blocks at the end of the program
def memcheck(file):
    text = file.read()

    p = re.compile(r'in use at exit: (\d+) bytes in (\d+) blocks')

    bytesInUse = int(p.search(text).group(1))
    blocks = int(p.search(text).group(2))

    return bytesInUse, blocks


makefile_dir = "directory of the makefile" # the directory of the makefile (like users/alex/coding/proj1)
os.system("cd " + makefile_dir) # changes the directory to that of the makefile
os.system("make") # compiles the code according to the makefile

name_of_the_executable = "name" # the name of the executable (like hw14)
path_to_test_case = "path" # the path to the test case from the current directory (like inputs/testcase1)
tempfile = "path/to/the/tempfile.txt" # the path to the tempfile
os.system("valgrind " + name_of_the_executable + " " + path_to_test_case + " --log-file=" + tempfile)
# previous statement executes valgrind on the code and writes the output to the tempfile

with open(tempfile) as f:
    bytes, blocks = memcheck(f) # opens the file and sends it to the memcheck funciton to get integer values

score -= bytes # decucts one percent from the score for each byte of memory leaked
