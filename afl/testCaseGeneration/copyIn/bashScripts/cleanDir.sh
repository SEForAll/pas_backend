#!/bin/bash
if [ $# -ne 1 ]; then
	echo "Variable Mismatch"
	exit 1
fi
cd $1
rm -r *
