#!/bin/bash

#Input Variables
#1: code dir, 2: inputs dir; 3: output dir, 4: fuzz time

if [ $# -ne 4 ]; then
	echo "Variable Mismatch"
	exit 1
fi
touch $3"/log.txt"
cd $1
rm -r CMakeCache.txt CMakeFiles Makefile cmake_install.cmake binary >> $3"/log.txt" 
cmake CMakeLists.txt >> $3"/log.txt"
make >> $3"/log.txt"
export AFL_NO_UI=1
afl-fuzz -i $2 -o $3 -V $4 -- $1"/binary" >> $3"/log.txt"
