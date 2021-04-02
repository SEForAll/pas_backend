from addToDB import *
import os
from datetime import datetime, timedelta


if __name__ == '__main__':
    path = '/home/agieson/git/pas_backend/testingfiles/'
    #profpath = f'{path}testAssignmentProf/'
    profpath = f'{path}hw2prof/'
    #profpath = f'{path}hw3prof/'



    expectedIn = f'{profpath}inputs'
    expectedOut = f'{profpath}outputs'
    makefile = f'{profpath}makefile'

    #submissionfile = f'{path}testsubmissionmemleak.zip'
    submissionfile = f'{path}hw2student.zip'
    #submissionfile = f'{path}hw3student.zip'


    weekfromnow = datetime.now() + timedelta(days=7)
    #assignmentname = 'test'
    assignmentname = 'hw2'
    #assignmentname = 'hw3'


    addAssignment(assignmentname, datetime.now(), weekfromnow, weekfromnow, datetime.now(), expectedIn, expectedOut, makefile)

    with open(submissionfile, 'rb') as file:
        grade, feedback = addSubmission('randomID', assignmentname, file)

    for line in feedback:
        print(line)

    print(f'\nyour score is: {grade}')
