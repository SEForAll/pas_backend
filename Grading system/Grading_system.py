# input: student file pass
# output: grade, a string about feedback

def grade_a_file_fun(inputfilepass):
    from compileable import *
    from diff import diff

    # Compileable
    compile_bool = compileable_fun('/home/tony/research/test.c')

    if (compile_bool == 0):  # If the input is not compile able, final grade = 0
        print("not compileable")
        grade_final = 0
        return grade_final

    # Diff
    hwNum = 1  # homework number, need from database
    subPath = '/Users/liang/PycharmProjects/pythonProject/research/diffs/'  # this is for testing, need from database
    diff(hwNum, subPath)  # homework number, path of files need diff

    # Check memory

    # Store final grade
        # front end will deal with storing final grade

    # clean the work space

    return grade_final
