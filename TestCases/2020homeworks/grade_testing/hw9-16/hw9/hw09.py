import unittest
import sys
import os

path2 = os.getcwd()

print(path2)

path1 = os.getcwd()

path1.append('../../../..')

os.chdir(path1)

from GradingInterface import interface
# import Gradinginterface.interface

print(111)
print(os.getcwd())

class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(path2, 'hw09.zip'),
                                            os.path.join(path2, '../../../HW09MergeSort'))
        print(graded.get_error_list())
        print(graded.get_grade())


if __name__ == '__main__':
    unittest.main() # run the unit test again ...
