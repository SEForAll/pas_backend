
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
        pass

    def clean_up(self):
        """
        Deletes unzipped items related to grading process

        :return: None
        """

    def __str__(self):
        return self.submission_folder_path


class TestCase:
    """
    A compilation of actions related to file operations a test case path

    :param test_case_path: path to the folder containing test casses
    """

    def __init__(self, test_case_path: str):
        self.test_case_path = test_case_path

    # Add any functions related to test case here that may need to be called by grade_submission

    def __str__(self):
        return self.test_case_path


def grade_submission(submission: str, test_case: str) -> GradedSubmission:

    user_grade = 0

    user_submission = Submission(submission)
    submission_test = TestCase(test_case)
    user_submission.setup()

    # Necessary grading code

    return GradedSubmission(user_grade)
