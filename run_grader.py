from TestCases.GradingInterface.interface import grade_submission
import sys
import os

def main(args):
    student_files = ''
    prof_files = ''

    if len(args) == 1:
        errormsg = 'ERROR: no student files directory specified\nplease specify the directory contining the student files to be graded'
        errormsg += f'\nEXAMPLE CALL: python3 {args[0]} users/alex/ECE264/hw01'
        return errormsg
    elif len(args) == 2:
        student_files = args[1]
        files = os.listdir(student_files)
        if 'MASTER' not in files:
            errormsg = 'ERROR: professor files not specified\nplease specify the directory containing the professor files or place it in the student directory and name it \'MASTER\''
            errormsg += f'\nEXAMPLE CALL: python3 {args[0]} users/alex/ECE264/hw01 users/alex/ECE264/prof_files/hw01'
            return errormsg
        prof_files = os.path.join(student_files, 'MASTER')
    elif len(args) == 3:
        student_files = args[1]
        prof_files = args[2]
    else:
        errormsg = 'ERROR: too many inputs specified\nplease only use 2 inputs maximum'
        errormsg += f'\nEXAMPLE CALL: python3 {args[0]} users/alex/ECE264/hw01 users/alex/ECE264/prof_files/hw01'
        return errormsg
    
    
    for file in os.listdir(student_files):
        if not file.endswith('.zip'):
            continue
        graded_obj = grade_submission(os.path.join(student_files, file), prof_files)
        grade = graded_obj.get_grade()
        feedback = graded_obj.get_error_list()

        # what to do with info?

        # test to make sure it works:
        print(f'--------------------\nresult of {file}:\n\t{feedback}\n\tgrade: {grade}%')

    return 0


if __name__ == '__main__':
    print(main(sys.argv))
    # how to test this program:
    # python3 run_grader.py ~/git/pas_backend/TestCases/2020homeworks/grade_testing/hw1-8/ ~/git/pas_backend/TestCases/2020homeworks/HW02Sort/
    