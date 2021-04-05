import unittest
from GradingInterface import interface
import os


class TestGradingInterface(unittest.TestCase):

    def test_grade_submission(self):
        graded = interface.grade_submission(os.path.join(os.getcwd(), 'sort.zip'),
                                            os.path.join(os.getcwd(), 'Sort2TestCases'))
        self.assertAlmostEqual(graded.get_grade(), 100)


if __name__ == '__main__':
    unittest.main()
