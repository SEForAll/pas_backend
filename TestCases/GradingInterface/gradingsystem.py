import os
from distutils.ccompiler import new_compiler
import filecmp
import re
import multiprocessing
import time

# 4. where do you run the program <-- line 132 of interface.py
def grade(path):
    """
    :param path: path to the project. ex) /users/alex/myfiles/project
    :type path: str

    :return: pointslist ([testcases, testcases passed, bytes leaked]), feedback
    """

    list_final = []  # list of feedback for the submission
    pointslist = []  # list of points for each section. order: [testcases, passed testcases, bytes leaked]

    debugging = False  # set to True to enable debugging print statements

    os.chdir(path)  # change the directory to the path of the project
    os.system('make clean >/dev/null 2>&1')  # get rid of files not needed

    if debugging:
        print('starting compile')

    # ---------------------------------
    # check that everything can compile

    if len(os.listdir(path)) == 0:  # if there are no files in the directory
        list_final.append('no files submitted')
        return None, list_final

    '''
    compiler = new_compiler()  # make the compiler object

    cmd = "gcc -std=c99 -g -Wall -Wshadow --pedantic -Wvla -Werror "
    for filename in os.listdir(path):  # For all files in the directory that end with .c
        if filename.endswith(".c"):
            cmd += filename+" "

    cmd+="-o new"
    result = os.system(cmd)   # Run the compile command, get the return value
    '''
    result = os.system("make")  # Run make

    filename = "hw"
    if result==0:
        list_final.append(f'{filename} compiled correctly! going to next step...')
    else:
        list_final.append(f'{filename} did not compile correctly, please check your files')
        return None, list_final
        exit
    if debugging:
        print('compile finished\nstarting diff')

    # this is the setup for the next few parts

    with open("Makefile", 'r') as f:  # open the Makefile
        text = f.read()  # read the contents of the Makefile

        # -----------------------
        # get the name of the executable

        # ex = re.compile(r'-o (\w+)')  # use regex to get the name of the executable made from the Makefile
        # match = ex.search(text)
        # if match is not None:
        #     executable = match.group(1)  # set the name of the executable as long as it is able to find it
        # else:
        #     list_final.append(
        #         'error when executing Makefile... contact your
        #         professor about this issue (name of executable can not be found)')
        #     return None, list_final

        # ------------------------
        # get the number of test cases to run

        num = re.compile(r'test(\d+):')  # pattern to find how many testcases there are
        match = num.findall(text)
        if len(match) != 0:  # if there is at least one match
            numberoftestcases = int(match[-1])
        else:
            list_final.append('error when executing Makefile... contact your '
                              'professor about this issue (number of test cases could not be found)')
            return None, list_final

        if numberoftestcases == 0:  # if there are no testcases
            list_final.append('error when executing Makefile... contact your '
                              'professor about this issue (number of test cases is not correct)')
            return None, list_final

        # ------------------------
        # get the valgrind statements to run

        valgrindstatements = []  # statements to run valgrind on (./hw14 inputs/input1)
        val = re.compile(r'(\./.+)')
        reglist = val.findall(text)
        for elem in reglist:
            temp = elem.split('>')[0]
            temp = elem.split('>>')[0]
            temp = elem.split('|')[0]
            valgrindstatements.append(temp)

    # -------------------------
    # Check diff

    passed = 0
    os.chdir(path)
    with open('empty.txt', 'w+') as f:  # make an empty file for comparison
        f.write('')

    with open('grade.txt', 'w+') as f:  # make a grading file
        f.write('')

    for i in range(1, numberoftestcases + 1):  # run the loop for each testcase
        # print(f'i is {i}')
        os.system('make clean >/dev/null 2>&1')  # get rid of unwanted
        os.system('make >/dev/null 2>&1')  # run 'make' in the console
        #os.system(f'make testcase{i} >/dev/null 2>&1')  # PROF MUST SEND THE OUTPUT OF THE DIFF COMMAND TO grade.txt !!
        # i can't route the output of the diff command, only the output of the testcase command
        # this must be done by the professor
        # ex) diff output1.txt expected1.txt > grade.txt
        try:
            checkfortimeout(os.system, args=[f'make test{i} >/dev/null 2>&1'])
        except TimeoutError:
            list_final.append(f'Test case {i} timed out')
            continue

        comp = filecmp.cmp('grade.txt', 'empty.txt', shallow=False)  # compare the files
        if comp is True:  # if the files match
            list_final.append(f"Test case {i} is correct!")
            passed += 1
        else:  # if the files don't mach
            list_final.append(f"Test case {i} is wrong...")

    pointslist.append(numberoftestcases)  # put numberoftestcases in the correct place in the pointslist
    pointslist.append(passed)  # put passed in the correct place in the pointslist
    list_final.append(f'{passed}/{numberoftestcases} test cases passed!')

    if debugging:
        print('diff finished\nstarting memcheck')

    # ----------------------------
    # Check memory
    bytesLeaked, blocksLeaked = memcheck(path, valgrindstatements)  # check leaked memory for each testcase

    # print(bytesLeaked)
    if bytesLeaked < 0:  # if bytes leaked is negative that means there was something wrong
        list_final.append('error when executing Makefile... contact your professor about this issue (valgrind not called correctly)')
        return None, list_final
    # else:
    #     list_final.append('makefile executed correctly!')

    if bytesLeaked > 0:  # if there was memory leak
        list_final.append(f'{bytesLeaked} byte(s) of memory leak present in the program')
    if bytesLeaked == 0:  # if there was no memory leak
        list_final.append('No memory leak!')

    pointslist.append(bytesLeaked)  # append bytesLeaked in the correct place in the pointslist

    if debugging:
        print('memcheck finished')

    os.system('make clean >/dev/null 2>&1')  # get rid of unwanted files
    os.remove('grade.txt')  # get rid of file now that grading is complete
    os.remove('empty.txt')  # get rid of file now that grading is complete

    return pointslist, list_final


def memcheck(makefile_dir, valgrindstatements):
    """
    :param makefile_dir: full directory to the makefile (starts with a '/' and does not include the makfile)
    :type makefile_dir: str
        example: /users/alex/desktop/project14
    :param valgrindstatements: list containing the statements to run valgrind on
    :type valgrindstatements: list
        example: ['./hw14 inputs/input1', ./hw14 inputs/input2]
    :return bytes: bytes of code leaked in the program
    :return blocks: blocks of code that leaked memory
    if the output is -1, -1: valgrind was not run correctly (make sure it's installed and working on your computer first)
    """

    os.chdir(makefile_dir)  # go to the folder where the makefile and other files are (essentially the project folder)

    os.system("make")# >/dev/null 2>&1")  # compiles the code according to the makefile

    tempfile = "tempfile.txt"  # name of the tempfile which will store the valgrind output

    bytesInUse = 0
    blocks = 0

    for statement in valgrindstatements:  # run through the valgrind statements
        #os.system(f'valgrind {statement} > {tempfile} 2>&1')
        try:
            checkfortimeout(os.system, args=[f'valgrind {statement} > {tempfile} 2>&1'])
            # previous statement executes valgrind on the executable and writes the output to the tempfile
        except TimeoutError:
            continue

        p = re.compile(r'in use at exit: (\d+) bytes in (\d+) blocks')  # regex for getting values from valgrind output

        with open(tempfile, 'r') as f:
            text = f.read()
            match = p.search(text)  # use regex to get number of bytes leaked and in how many blocks
            if match is None:
                return -1, -1  # return this if valgrind is not called properly (might happen bc i wrote this on mac)
            bytesInUse += int(match.group(1))  # put regex groups from the match into variables and cast to integers
            blocks += int(match.group(2))

        os.remove(tempfile)  # remove the files we created as they only pertain to this function

    return bytesInUse, blocks


def checkfortimeout(func, args=None, timeout=5):
    """
    runs a function and raises TimeoutError if the specified time limit is reached
    :param func: funciton that could timeout
    :type func: function
    :param args: arguments to pass to the function (defaults to None)
    :type args: list
    :param timeout: number of seconds to trigger a timeout (defaults to 5)
    :type timeout: int
    :return:
    """

    process1 = multiprocessing.Process(target=time.sleep, args=[timeout])  # sets timeout process
    if args is None:  # sets process that might timeout
        process2 = multiprocessing.Process(target=func)
    else:
        process2 = multiprocessing.Process(target=func, args=args)

    process1.start()  # start both processes
    process2.start()
    while process1.is_alive():  # while the timeout process is still running
        if process2.is_alive() is False:  # if the function is done running, return the function
            return
    process2.terminate()  # if the timeout process is finished and the function is not, raise an error
    raise TimeoutError("the program timed out")
