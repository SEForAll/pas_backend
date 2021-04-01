from addToDB import *
import os

if __name__ == '__main__':
    path = '/home/agieson/git/pas_backend/testingfiles/'
    studentpath = f'{path}testAssignmentStudent'
    profpath = f'{path}testAssignmentProf'

    expectedIn = f'{profpath}/inputs'
    expectedOut = f'{profpath}/outputs'
    makefile = f'{profpath}/makefile'

    score, feedback = grade_fun(studentpath, expectedIn, expectedOut, makefile)

    for line in feedback:
        print(line)
    
    print(f'\nyour score is: {score}')


