import unittest
from GradingInterface import interface
import os

path = os.getcwd()

def testhw02():
    graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw1-8/hw2.zip'),
                                        os.path.join(path, '2020homeworks/HW02Sort'))
    print(f'grade for hw02 is {graded.get_grade()}')

    return graded.get_error_list()

# ...

if __name__ == '__main__':
    testhw02()
    # ......
