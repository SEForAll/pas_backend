#!/usr/bin/env python3

from TestCases.GradingInterface.interface import *
import sys
import os
import argparse

# submission file, test case folder, hw tag, user id, output directory
# Plan:
#   Try it on one test case with a known number of tests
#   Hardcode the weights
GRADE_FILE = 'grade.txt'
FEEDBACK_FILE = 'feedback.txt'

def parse_args(args):

    # Checks if the argument is a path to a directory
        def dir_path(path):
            if not os.path.isdir(path):
                raise ValueError
            return path
        # Checks if the argument is a path to a zip file
        def zipfile_path(path):
            if not path.endswith('.zip') or not os.path.isfile(path):
                raise ValueError
            return path

        parser = argparse.ArgumentParser(description='CMD line interface for grading a homework submission')
        parser.add_argument('submission_zip', help='HW submission ZIP file', type=zipfile_path)
        parser.add_argument('test_cases_dir', help='Folder with test cases to grade against', type=dir_path)
        parser.add_argument('hw_tag', help='Homework tag')
        parser.add_argument('user_id', help='Student\'s user id')
        parser.add_argument('out_dir', help=f'Directory to place {GRADE_FILE} and {FEEDBACK_FILE}', type=dir_path,
            default=os.getcwd())

        args = parser.parse_args(args)
        return args

def grade_hw(zip_file_path, test_cases_dir_path):
    graded_obj = grade_submission(zip_file_path, test_cases_dir_path)
    grade = graded_obj.get_grade()
    feedback = graded_obj.get_error_list()

    return grade, feedback

def write_grade(grade, hw_tag, user_id, out_dir):
     with open(os.path,join(out_dir, GRADE_FILE), 'w') as f:
        f.write(hw_tag)
        f.write(user_id)
        f.write(grade)

def write_feedback_list(feedback_list, hw_tag, user_id, out_dir):
    with open(os.path.join(out_dir, FEEDBACK_FILE), 'w') as f:
        f.write(hw_tag)
        f.write(user_id)
        f.write(feedback_list.join('\n'))

if __name__ == '__main__':
    #args = parse_args(sys.argv[1:])
    #grade, feedback_list = grade_hw(args.submission_zip, args.test_cases_dir)

    #write_grade(grade, args.hw_tag, args.user_id, args.out_dir)
    #write_feedback_list(feedback_list, args.hw_tag, args.user_id, args.out_dir)

    curr_dir = os.getcwd()
    grade, feedback_list = grade_hw(os.path.join(curr_dir, 'TestCases/2020homeworks/grade_testing/hw17-21/hw17/hw17.zip'),
                                    os.path.join(curr_dir, 'TestCases/2020homeworks/HW17Huffman1'))
    write_grade(grade, 'test tag', 'fake user id', curr_dir)
    write_feedback(feedback_list, 'test tag', 'fake user id', curr_dir)

