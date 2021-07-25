#!/bin/bash

# Initialize file the program will edit with text
echo "Unedited" > ./edit_a_file/file.txt
echo "Contents of ./edit_a_file/file.txt before grading..."
cat ./edit_a_file/file.txt

# Create a copy of the homework submission containing the dangerous code
# We need to copy from a backup since grade_submission deletes the homework folders after grading
cp -R ./edit_a_file/backup ./edit_a_file/sort

# Run grade_submission.py
../grade_submission.py ./edit_a_file/sort/ ../TestCases/2020homeworks/HW02Sort hw02 testuser .

# Show that the program edited the file
echo "Contents of ./edit_a_file/file.txt after grading..."
cat ./edit_a_file/file.txt

# cleanup
rm grade.txt feedback.txt
