# ***
# *** DO NOT modify this file 
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_ELIMINATE

SRCS = main.c eliminate.c
OBJS = $(SRCS:%.c=%.o)

main: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o main

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: test1 test2 test3 

testcase1: main
	./main 6 3 > output1
	diff output1 expected/expected1 > grade.txt

testcase2: main
	./main 4 25 > output2 # should be 6 4 but changed to cause a test case to fail... for demonstration purposes
	diff output2 expected/expected2 > grade.txt

testcase3: main
	./main 25 7 > output3
	diff output3 expected/expected3 > grade.txt

clean: # remove all machine generated files
	rm -f main *.o output?


