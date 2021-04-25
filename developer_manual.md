## Introduction
&emsp;The purpose of this developer manual is to help a developer understand our code in detail and be able to add more functions to our grading system. 
If you are only interested in how to use our system and do not plan to change any function, please read the [user_manual](User_manual).  
&emsp;In this developer manual, we will mainly focuse on introducing [Grading System Code](TestCases/GradingInterface/gradingsystem.py) and its 
corresponding [Grading System Interface](TestCases/GradingInterface/interface.py). Although backend has a database, it is not implemented. Frontend has the actual
database we are using for our system.

## Table of contents
* [How_to_use_grading_system_interface](#How_to_use_grading_system_interface)
* [How_does_our_code_grade_hw](#How_does_our_code_grade_hw)
* [Date_flow](#Date_flow)
* [Code_location](#Code_location)

## How_to_use_grading_system_interface


## How_does_our_code_grade_hw
&emsp;First of all, you need to open this file, [gradingsystem.py](TestCases/GradingInterface/gradingsystem.py). Basically, we use linux terminal commands to grade
students' homework. Instead of manually type it out in a terminal, we will let the grading system do it for us. After the function, grade, be called, this is what
our code will do.  
&emsp; 0. We need a Makefile that had been seted up already by the professor before calling the function. Check the [Makefile template](grading_system_helper/Makefile).    
&emsp; 1. (line 17-23) We will create two lists, one is used to store the feedback for submission. The other one is used to store points for each section. 
Then we change the directory to the path of the project.  
&emsp; 2. (line 28-83) We will check if everything can compile.  
&emsp;&emsp; There are enough comments in gradingsystem.py to help you understand how to check if everything can compile.  
&emsp; 3. (line 94-128) We will run diff command on every test cases specified in the Makefile. Then we will compare the output of the diff commant with an empty file.
If the output of the diff commant is not empty, the test case is wrong. Then, We will store the feedback in the list_final list and the grade in the pointslist list.  
&emsp; 4. (line 94-128) 


## Date_flow


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
