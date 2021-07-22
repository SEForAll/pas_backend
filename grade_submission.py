#!/usr/bin/env python3

from TestCases.GradingInterface.interface import *
import sys
import os
import argparse

GRADE_FILE = 'grade.txt'
FEEDBACK_FILE = 'feedback.txt'

def parse_args(args):
    """
    utilize argparse to define the arguments needed to grade files

    :param args: holds all the defined arguments
    """
    def force_absolute(path):
        return path if path[0] == '/' else os.path.join(os.getcwd(), path) #find absolute path relative to directory

    def dir_path(path):
        """
        Checks if the argument is a path to a directory

        :param path: relative or absolute path to a directory
        """
        path = force_absolute(path) #try to obtain correct path
        if not os.path.isdir(path): #if path does not exist, raise an error
            raise ValueError
        return path
 
    def zipfile_path(path):
        """
        Checks if the argument is a path to a zip file

        :param path: relative or absolute path to a zip file
        """
        path = force_absolute(path) #try to obtain correct path
        if not path.endswith('.zip') or not os.path.isfile(path): #if the path is not a zip file or does not exist, raise an error
            raise ValueError
        return path

    def zipfile_or_dir_path(path):
        """
        Checks if the argument is a path to a directory or a zip file

        :param path: relative or absolute path to a zip file/directory
        """
        try:
            path = zipfile_path(path)
        except ValueError as e:
            path = dir_path(path)
        return path

    # define the arguments to be used with argparse
    parser = argparse.ArgumentParser(description='CMD line interface for grading a homework submission')
    parser.add_argument('submission_path', help='HW submission folder or ZIP file', type=zipfile_or_dir_path)
    parser.add_argument('test_cases_dir', help='Folder with test cases to grade against', type=dir_path)
    parser.add_argument('hw_tag', help='Homework tag')
    parser.add_argument('user_id', help='Student\'s user id')
    parser.add_argument('out_dir', help=f'Directory to place {GRADE_FILE} and {FEEDBACK_FILE}', type=dir_path,
        default=os.getcwd())

    args = parser.parse_args(args) #pass in the user-defined arguments into args
    return args

def grade_hw(zip_file_path, test_cases_dir_path):
    """
    use the grade_submission function within interface.py to get a object containing grades and feedback

    :param zip_file_path: path to zip file containing hw to grade
    :param test_cases_dir_path: path to test case to use
    :return: grade and feedback
    """
    graded_obj = grade_submission(zip_file_path, test_cases_dir_path) #return graded object containing the grade information
    return graded_obj.get_grade(), graded_obj.get_error_list()

def write_grade(grade: float, hw_tag: str, user_id: str, out_dir: str) -> None:
    """
    write the grade information to a .txt file in the out directory

    :param grade: float of the percentage correct
    :param hw_tag: hw tag to write in the txt file
    :param user_id: user id to write in the txt file
    :param out_dir: str directory of where to create the txt file
    """
    with open(os.path.join(out_dir, GRADE_FILE), 'w') as f: #write the grade information to a text file called grade.txt in the output directory
        f.write(f'{hw_tag}\n')
        f.write(f'{user_id}\n')
        f.write(f'{grade:.2f}%\n')

def write_feedback(feedback: list, hw_tag: str, user_id: str, out_dir: str) -> None:
    """
    write the feedback information to a .txt file in the out directory

    :param feedback: list of the percentage correct
    :param hw_tag: hw tag to write in the txt file
    :param user_id: user id to write in the txt file
    :param out_dir: str directory of where to create the txt file
    """
    feedback = '\n'.join(feedback) #add end to feedback string
    with open(os.path.join(out_dir, FEEDBACK_FILE), 'w') as f: #write the feedback to a text file called feedback.txt in the output directory
        f.write(f'{hw_tag}\n')
        f.write(f'{user_id}\n')
        f.write(f'{feedback}\n')

if __name__ == '__main__':
    """
    if valid, take the arguments and call the necessary functions to grade and output the text files
    """
    args = parse_args(sys.argv[1:])
    grade, feedback = grade_hw(args.submission_path, args.test_cases_dir) #grade the hw from the zip file

    write_grade(grade, args.hw_tag, args.user_id, args.out_dir) #grade and write grade info to txt file
    write_feedback(feedback, args.hw_tag, args.user_id, args.out_dir) #obtain feedback and write feedback to txt file

 # ./grade_submission.py TestCases/2020homeworks/grade_testing/hw9-16/hw15/hw15.zip TestCases/2020homeworks/HW15BinaryTree1 fake_tag fake_id .
 # example of command to run code using hw15 and placeholder tags
