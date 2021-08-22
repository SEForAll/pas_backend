# pas_backend
This readme is used to help you allocate where is the code. It is not used to teach you how to use our system. If you want to know how to use our system, go to the [documentation](documentation) folder.  
&emsp;Backend has all the functionality code for program analysis. There are four main chunk of files in this repository:  
&emsp;1. Database (located in [databasefiles](databasefiles) folder)  
&emsp;2. Grading system code (located in [TestCases/GradingInterface](TestCases/GradingInterface) folder)  
&emsp;3. Grading system interface (located in [TestCases/GradingInterface](TestCases/GradingInterface) folder)  
&emsp;4. Documentation (located in [documentation](documentation) folder)  

There is also a folder called 'grading_system_trash' folder used to store draft files.

## Table of folders
* [databasefiles](#databasefiles)
* [TestCases](#TestCases)
* [Documentation](#Documentation)

## databasefiles
This folder stores code related to database. We used peewee(sqlite3) to set up our database.  
&emsp;- database.py  
&emsp;&emsp;This file contains the peewee code.  

&emsp;- addToDB.py  
&emsp;&emsp;This file contains some helper functions to manage database.  

## TestCases
This folder stores code of grading system, code of grading system interface, code of changing grading parameters feature, and a test folder of the grading system.  

&emsp;- [equation.py](TestCases/GradingInterface/equation.py)  
&emsp;&emsp;This file contains code of changing grading parameters feature.  

&emsp;- [gradingsystem.py](TestCases/GradingInterface/gradingsystem.py)  
&emsp;&emsp;This file contains code of grading system. This is the core file of backend. The grading system will take path to the project as input. The grading system will output pointslist and feedback. The grading system can check: 1. Is the student file compileable? 2. Can the student file output the expected output given the expected input? 3. How many byte does the student file leak? 4. Will the student file get into an infinite loop?  
&emsp;- [interface.py](TestCases/GradingInterface/interface.py)   
&emsp;&emsp;This file contains code of grading system interface. Meaning frontend user can use grading system through calling functions in this file. There is no need to call functions in gradingsystem.py. 

&emsp;- [grade_submission.py](grade_submission.py)   
&emsp;&emsp;This file contains code of grading system interface as well as the means to input arguments to output two text files, one containing the grade and the other the feedback for a specified homework of a user. It serves as a very streamlined way to run the grading system through a single command. Running the file with the -h or -help argument will show the arguments needed for the code to function.

&emsp;- .[2020homeworks](TestCases/2020homeworks)  
&emsp;&emsp;This folder is the example "professor files" folder, you need to set you a folder like this to be able to test our system. For each homework, you need to have: 1. Expected output. 2. Inputs. 3. A Makefile according to our [Makefile_template](documentation/Makefile) (It is currently setted up for ECE264 2020 homeworks)    

&emsp;- .[Testing_grading_system](TestCases)  
&emsp;&emsp;After you set up the "professor files" folder, you can write code that will run our grading system. There are python files named by hw02 to hw21, such as hw02.py. Run these programs by using command like "python3 hw02.py" to get scores and feedbacks for students' homeworks.  

&emsp;- [jsonfile_generator.py](TestCases/jsonfile_generator.py)   
&emsp;&emsp;This file contains code of generating example json file.

## Documentation
This folder stores three important files that can help you understand our system.  

&emsp;- [Makefile_template](documentation/Makefile)  
&emsp;&emsp;By reading this file, you can know how to write Makefile for our grading system. (you need to have a basic understanding of makefile before reading this template)  

&emsp;- [User_manual](documentation/User_manual.md)  
&emsp;&emsp;By reading this file, you can have a better understanding of our system as a user(student).  

&emsp;- [developer_manual](documentation/developer_manual.md)  
&emsp;&emsp;By reading this file, you can have a better understanding of our system as a developer(research team student).  
