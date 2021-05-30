import unittest
from GradingInterface import interface
import os

path = os.getcwd()

class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(path, 'sort.zip'),
                                            os.path.join(path, 'Sort2TestCases'))
        print(graded.get_error_path())
        self.assertAlmostEqual(graded.get_grade(), 100)

    def test_grade_submission2(self):
        graded = interface.grade_submission(os.path.join(path, 'hw07.zip'),
                                            os.path.join(path, 'hw7TestCase'))
        print(graded.get_error_path())
        self.assertAlmostEqual(graded.get_grade(), 100)


if __name__ == '__main__':
    unittest.main() # run the unit test again ...
