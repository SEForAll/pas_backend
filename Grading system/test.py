from ServerFiles.Grading_system import grade_fun
import filecmp
import os

yourpath = '/Users/alexgieson/Desktop/'

path = f'{yourpath}testAssignmentStudent'
expectedIn = f'{yourpath}testAssignmentProf/inputs'
expectedOut = f'{yourpath}testAssignmentProf/outputs'
makefile = f'{yourpath}testAssignmentProf/makefile'

score, feedback = grade_fun(path, expectedIn, expectedOut, makefile)

for line in feedback:
    print(line)
print(f'\nyour score is: {score}')

# os.chdir(path)
# comp = filecmp.cmp('temp.txt', '/Users/alexgieson/Desktop/hw14/outputs/output2.txt', shallow=False)
# print(comp)

