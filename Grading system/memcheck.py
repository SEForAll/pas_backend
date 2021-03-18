import re
import os


# file --> a file that has all the valgrind information on it (not verbose)
# returns how many bytes are in use and in how many blocks at the end of the program
# if the output is -1, -1: the name of the executable cannot be found
# if the output is -2, -2: valgrind was not run correctly (make sure it's installed and working on your computer first)
def memcheck(makefile_dir, path_of_testcase):
    # this might get a little confusing so i will explain now
    # path_of_testcase is the path of the test case that includes the testcase itself
        # an example of this would be this/is/a/path/to/the/test/case/testcase.txt
    # path_to_testcase is simply the path to the test case, which does not include the testcase file at the end
        # an example of this could be this/is/a/path/to/the/test/case

    if path_of_testcase != 0:
        t = re.compile(r'/(\w+.\w+)$')  # regex that will get the testcase file name

        name_of_test_case = t.search(path_of_testcase).group(1)  # get the filename of the testcase
        path_to_test_case = path_of_testcase.replace('/' + name_of_test_case, '')
        # remove the filename from the path to just get the path

        os.chdir("../../../../../../../../../../../../../../../../../..")  # this should be enough to get to the root folder
        os.chdir(path_to_test_case)  # go to the folder where the test case is
        with open(name_of_test_case) as f:  # open the specified test case
            testcase = f.read()  # read the test case and store the data for later

    os.chdir("../../../../../../../../../../../../../../../../../..")  # again, hoping to get to the root folder
    os.chdir(makefile_dir)  # go to the folder where the makefile and other files are (essentially the project folder)

    with open("makefile", 'r') as f:  # open the makefile
        text = f.read()
        ex = re.compile(r'-o (\w+)')  # use regex to get the name of the executable made from the makefile
        match = ex.search(text)
        if match is not None:
            executable = match.group(1)  # set the name of the executable as long as it is able to find it
        else:
            return -1, -1  # happens when the name of the executable cannot be found from the makefile

    os.system("make")  # compiles the code according to the makefile

    tempfile = "tempfile.txt"  # name of the tempfile which will store the valgrind output

    if path_of_testcase != 0:
        testfile = "testcase.txt"
        with open(testfile, 'w') as f:
            f.write(testcase)  # writes the testcase into a file in the current directory

        os.system("valgrind ./" + executable + " " + testfile + " > " + tempfile + " 2>&1")
        # previous statement executes valgrind on the executable and writes the output to the tempfile
    else:
        os.system("valgrind ./" + executable + " > " + tempfile + " 2>&1")

    p = re.compile(r'in use at exit: (\d+) bytes in (\d+) blocks')  # regex for getting values from valgrind output

    with open(tempfile, 'r') as f:
        text = f.read()
        match = p.search(text)  # use regex to get number of bytes leaked and in how many blocks
        if match is None:
            return -2, -2  # return this if the valgrind is not called properly (might happen bc i wrote this on mac)
        bytesInUse = int(match.group(1))  # put regex groups from the match into variables and cast to integers
        blocks = int(match.group(2))

    os.remove(tempfile)  # remove the files we created as they only pertain to this function
    os.remove(testfile)

    return bytesInUse, blocks


### EXAMPLE CODE THAT WORKS ON ALEX'S COMPUTER (macOS Big Sur)

makefile_dir = "Users/alexgieson/Desktop/hw14"  # the directory of the makefile starting at the root
path_of_test_case = "Users/alexgieson/Desktop/hw14/inputs/input1.txt"  # the path to the test case from root

bytes, blocks = memcheck(makefile_dir, path_of_test_case)  # opens the file and sends it to the memcheck funciton to get integer values

if bytes >= 0:
    print(f'you have {bytes} bytes of memory leak')
elif bytes == -1:
    print('the name of the executable could not be found')
elif bytes == -2:
    print('valgrind did not output to the correct file')
