import unittest
import sys
import os

path2 = os.getcwd()

print(111)
print(path2)
print(111)

'''
sys.path.append("../../../..")

print(path)

from GradingInterface import interface
# import Gradinginterface.interface

class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(path2, 'hw09.zip'),
                                            os.path.join(path2, '../../../HW09MergeSort'))
        print(graded.get_error_list())
        print(graded.get_grade())
'''

if __name__ == '__main__':
    unittest.main() # run the unit test again ...
