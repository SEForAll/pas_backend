# pas_backend
Backend has all the functionality code for program analysis. There are three main chunk of code in this repository:
    1. Database (located in 'databasefiles' folder)
    2. Grading system code (located in 'TestCases/GradingInterface' folder)
    3. Grading system interface (located in 'TestCases/GradingInterface' folder)

There is also a folder called 'grading_system_helper' used to store draft files of Grading system code and the Makefile template.

## Table of contents
* [databasefiles](#databasefiles)
* [grading_system_helper](#grading_system_helper)
* [TestCases](#TestCases)

## databasefiles
This folder stores code related to database. We used peewee(sqlite3) to set up our database. 
    - database.py
        This file contains the peewee code.
    - addToDB.py
        This file contains some helper functions to manage database.

## grading_system_helper
This folder stores draft codes of Grading system code and the Makefile template.
    - grading_system_helper/draftfiles
        This folder stores draft codes of Grading system code.
    - Makefile
        This is the template for the Makefile that is one of the key elements of the grading system code. Any developer should read   this template before modifying gradingsystem.py. Any professor user should read this template to create the corresponding Makefile of an assignment.

## TestCases


# Todo

## Directory Maintenance

- There are lots of duplicate files, please remove duplicates and condense into one file per filename. If you find 
    yourself duplicating files, you should create a branch instead.
- No filenames should have spaces. Use snake_case for file names.
- Fill in this readme to describe (at a high level) what each file/folder is used for.


## Database Maintenance

- Frontend is maintaining OAUTH data for users, so backend should remove models
related to OAUTH and have just one table to store user ID.
- Consider consolidating databases and filesystem with frontend--this may make submission processing easier.


