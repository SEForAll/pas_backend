from .addToDB import *
import os
from datetime import datetime, timedelta


if __name__ == '__main__':
    path = '/home/agieson/git/pas_backend/testingfiles/'
    profpath = f'{path}testAssignmentProf/'

    expectedIn = f'{profpath}inputs'
    expectedOut = f'{profpath}outputs'
    makefile = f'{profpath}makefile'

    submissionfile = f'{path}testsubmission.zip'

    weekfromnow = datetime.now() + timedelta(days=7)
    assignmentname = 'test'

    addAssignment(assignmentname, datetime.now(), weekfromnow, weekfromnow, datetime.now(), expectedIn, expectedOut, makefile)

    with open(submissionfile, 'rb') as file:
        grade, feedback = addSubmission('random ID', assignmentname, file)

    for line in feedback:
        print(line)

    print(f'\nyour score is: {grade}')