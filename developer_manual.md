## Introduction
&emsp;The purpose of this developer manual is to help a developer understand our code in detail and be able to add more functions to our grading system. 
If you are only interested in how to use our system and do not plan to change any function, please read the [user_manual](User_manual).  
&emsp;In this developer manual, we will mainly focuse on introducing [Grading System Code](TestCases/GradingInterface/gradingsystem.py) and its 
corresponding [Grading System Interface](TestCases/GradingInterface/interface.py). Although backend has a database, it is not implemented. Frontend has the actual
database we are using for our system.

## Table of contents
* [How_does_grading_system_interface_work](#How_does_grading_system_interface_work)
* [How_does_our_code_grade_hw](#How_does_our_code_grade_hw)
* [Date_flow](#Date_flow)
* [Code_location](#Code_location)

## How_does_grading_system_interface_work
First of all, you need to open this file, [interface.py](TestCases/GradingInterface/interface.py). We defined three (classes? objects?). Class GradedSubmission is used to (). Class Submission is used to (). Class TestCase is used to (). 

(Which function we should call. What parameters we need to pass into the function.) 

## How_does_our_code_grade_hw
&emsp;First of all, you need to open this file, [gradingsystem.py](TestCases/GradingInterface/gradingsystem.py). Basically, we use linux terminal commands to grade students' homework. Instead of manually type it out in a terminal, we will let the grading system do it for us. After the function, grade, be called, this is what our code will do.  
&emsp; 0. We need a Makefile that had been seted up already by the professor before calling the function. Check the [Makefile template](grading_system_helper/Makefile).    
&emsp; 1. (line 17-23) We will create two lists, one is used to store the feedback for submission. The other one is used to store points for each section. 
Then we change the directory to the path of the project.  
&emsp; 2. (line 28-83) We will check if everything can compile. There are enough comments in gradingsystem.py to help you understand how to check if everything can compile.  
&emsp; 3. (line 94-128) We will run diff command on every test cases specified in the Makefile. Then we will compare the output of the diff commant with an empty file. If the output of the diff commant is not empty, the test case is wrong. Then, We will store the feedback in the list_final list and the grade in the pointslist list.  
&emsp; 4. (line 134-203) We will check memory error on every test cases specified in the Makefile. If there is memory leak, we will use regex to get number of bytes leaked and in how many blocks. Then, we will store the feedback in the list_final list and the grade in the pointslist list.  
&emsp; 5. (line 206-230) For each terminal command we called, we call function, checkfortimeout, to set a timeout for the command to prevent getting into infinite loop.

## Date_flow
Use(something) call (a function) in [interface.py](TestCases/GradingInterface/interface.py), then 


## Code_location
&emsp;- Database  
&emsp;&emsp;[database.py](databasefiles/database.py)  
&emsp;&emsp;[addToDB.py](databasefiles/addToDB.py)  

&emsp;- Grading System  
&emsp;&emsp;[gradingsystem.py](TestCases/GradingInterface/gradingsystem.py)  
&emsp;&emsp;[interface.py](TestCases/GradingInterface/interface.py)  
&emsp;&emsp;[equation.py](TestCases/GradingInterface/equation.py)  
&emsp;&emsp;[Makefile](grading_system_helper/Makefile)  

For detail description, please read [readme](README.md)
