from zipfile import ZipFile
import re
import os
from .gradingsystem import grade
from .equation import calculate_grade
import json

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
    def __init__(self, graded_score, error_file=None, dictionary=None):

        self.graded_score = graded_score
        self.error_file = None
        self.error_list = error_file
        self.dict = dictionary

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

    def get_error_list(self):
        return self.error_list

    def get_dict(self):
        return self.dict


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


def grade_submission(submission: str, test_case: str, hourslate=0, weights=None) -> GradedSubmission:
    """
    grade the submission and return a GradedSubmission object with all info stored inside, grade is calculated using
    the specified equation (default: 100*(p/t)-m-10*l)

    :param submission: path to the submission zipfile
    :type submission: str
    :param test_case: path to the test case (unzipped folder)
    :type test_case: str
    :param hourslate: how many hours late the submission was submitted
    :type hourslate: float
    :param weights: a dictionary that contains the weights of each testcase and the memoryleak (ex: {'test1': 40, 'test2' 60, 'mem_coef': 2})
    :type weights: dict
    :return:
    """

    user_submission = Submission(submission)  # this holds the path to the zip file
    submission_testcases = TestCase(test_case)
    user_submission.setup()  # unzips submission into a folder and sets folder path

    submission_testcases.copyfiles(user_submission.submission_folder_path)  # copies prof files to submission dir

    if weights is None:
        if 'weights.json' in os.listdir(test_case):
            with open(os.path.join(test_case, 'weights.json')) as f:
                weights = json.load(f)['weights']  # read the wieghts part from the json
                weights = {list(elem.keys())[0]: elem[list(elem.keys())[0]] for elem in weights}  # combine the dictionaries (json file params are each their own dict)

                for key in weights.keys():
                    try:
                        weights[key] = float(weights[key])
                    except ValueError:
                        user_feedback = 'error when executing Makefile... contact your professor about this issue (weights.json includes non integer or float point values)'
                        return GradedSubmission(0, user_feedback)
                    except TypeError:
                        if type(weights[key]) is list:
                            weights[key] = float(weights[key][0])

    if 'late_coef' in weights.keys():
        if weights['late_coef'] * hourslate >= 100:
            return GradedSubmission(0, f'submission submitted {hourslate} hours past the deadline resulting in a 0%')
    
    print(weights)

    os.chdir(user_submission.submission_folder_path)

    ## get the number of test cases so that we can check if the weights dict is correct
    numberoftestcases = 0
    with open("Makefile", 'r') as f:  # open the Makefile
        text = f.read()  # read the contents of the Makefile

        # get the number of test cases to run

        num = re.compile(r'test(\d+):')  # pattern to find how many testcases there are
        match = num.findall(text)
        if len(match) != 0:  # if there is at least one match
            numberoftestcases = int(len(match))
        else:  # if the number of test cases can not be found from the makefile
            user_feedback = 'error when executing Makefile... contact your professor about this issue (number of test cases could not be found)'
            return GradedSubmission(0, user_feedback)

        if numberoftestcases == 0:  # if there are no testcases
            user_feedback = 'error when executing Makefile... contact your professor about this issue (number of test cases is not correct)'
            return GradedSubmission(0, user_feedback)
    
    if weights is None:  # if weights is empty, make it from scratch
        for num in range(1, numberoftestcases + 1):
            weights[f'test{num}'] = 1
        weights['mem_coef'] = 1
        weights['late_coef'] = 1
    else:  # if weights is not empty, make sure it has all the right parts
        keys = weights.keys()
        for num in range(1, numberoftestcases + 1):
            if f'test{num}' not in keys:
                weights[f'test{num}'] = 1
        if 'mem_coef' not in keys:
            weights['mem_coef'] = 1
        if 'late_coef' not in keys:
            weights['late_coef'] = 1

        for key in keys:
            try:
                weights[key] = float(weights[key])
            except ValueError:
                user_feedback = 'error when executing Makefile... contact your professor about this issue (weights.json includes non integer or float point values)'
                return GradedSubmission(0, user_feedback)
            except TypeError:
                if type(weights[key]) is list:
                    weights[key] = float(weights[key][0])

    points, user_feedback, testcases_dict = grade(user_submission.submission_folder_path, weights)  # grades submission and gets point values

    if points is None:  # returns none if there was something wrong when grading (student side)
        user_submission.clean_up()  # deletes copied files
        return GradedSubmission(0, user_feedback)

    user_submission.clean_up()  # deletes copied files

    return GradedSubmission(round(points - weights['late_coef'] * hourslate, 2), user_feedback, dictionary=testcases_dict)

