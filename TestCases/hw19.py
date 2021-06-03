import unittest
from GradingInterface import interface
import os

path = os.getcwd()

print(path)

class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(path, '2020homeworks/grade_testing/hw17-21/hw19/hw19.zip'),
                                            os.path.join(path, '2020homeworks/HW19Maze'))
        print(graded.get_error_list())
        print(graded.get_grade())


if __name__ == '__main__':
    unittest.main() # run the unit test again ...