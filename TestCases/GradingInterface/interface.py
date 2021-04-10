from zipfile import ZipFile
import re
import os
from .gradingsystem import grade
from .equation import calculate_grade

# This is a python module. Outside of this directory:
# from GradingInterface import interface

class GradedSubmission:
    """
    Holds all information and methods related to the completed grading of an assignment

    :param graded_score: Score from 0 to 100
    :type graded_score: float
    :param error_file: Path to file containing error output from grading process, optional
    :type error_file: str
    """
    def __init__(self, graded_score, error_file=None):

        self.graded_score = graded_score
        self.error_file = error_file

    def get_grade(self):
        return self.graded_score

    def get_error_path(self):
        if self.error_file is None:
            raise AttributeError("No error file attached to this graded submission")

        return self.error_file

    def get_error_text(self):
        if self.error_file is None:
            raise AttributeError("No error file attached to this graded submission")

        with open(self.error_file) as f:
            return f.readlines()


class Submission:

    def __init__(self, submission_path: str):
        """
        A compilation of actions related to file operations on a user submission

        :param submission_path: path to the zip file of user's submission
        """
        self.submission_zip_path = submission_path
        self.submission_folder_path = ''  # The path to unzipped submission

    def setup(self):
        """
        Unzips the submission

        :return: None
        """

        p = re.compile(r'^(.+).zip$')
        match = p.search(self.submission_zip_path)
        self.submission_folder_path = match.group(1)

        if os.path.isdir(self.submission_folder_path) is False:
            os.makedirs(self.submission_folder_path)

        with ZipFile(self.submission_zip_path, 'r') as submission:
            submission.extractall(self.submission_folder_path)

        return

    def clean_up(self):
        """
        Deletes unzipped items related to grading process

        :return: None
        """
        os.system(f'rm -r {self.submission_folder_path}')

        return

    def __str__(self):
        return self.submission_folder_path


class TestCase:
    """
    A compilation of actions related to file operations a test case path

    :param test_case_path: path to the folder containing test cases
    """

    def __init__(self, test_case_path: str):
        """

        :param test_case_path: path to the folder that the professor uploaded
        """
        self.test_case_path = test_case_path
        self.files = os.listdir(test_case_path)

    def copyfiles(self, submission_dir):
        os.chdir(self.test_case_path)
        for file in self.files:
            os.system(f'cp -r {file} {submission_dir}')

    def removefiles(self, submission_dir):
        os.chdir(submission_dir)
        for file in self.files:
            os.system(f'rm -r {file}')

    def __str__(self):
        return self.test_case_path


def grade_submission(submission: str, test_case: str, equation="100*(p/t)-m-10*l") -> GradedSubmission:
    """
    grade the submission and return a GradedSubmission object with all info stored inside

    :param submission: path to the submission zipfile
    :type submission: str
    :param test_case: path to the test case (unzipped folder)
    :type test_case: str
    :return:
    """

    user_submission = Submission(submission)  # this holds the path to the zip file
    submission_testcases = TestCase(test_case)
    user_submission.setup()  # unzips submission into a folder and sets folder path

    submission_testcases.copyfiles(user_submission.submission_folder_path)

    pointslist, user_feedback = grade(user_submission.submission_folder_path)

    pointslist.append(0)  # pointslist.append(dayslate) --> this will get added when we figure that out

    user_submission.clean_up()  # deletes copied files

    return GradedSubmission(calculate_grade(pointslist, equation), user_feedback)

