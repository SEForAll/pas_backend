# ***
# *** DO NOT modify this file 
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_CONVERT -DTEST_MAIN  -DTEST_READLIST -DTEST_DELETELIST -DTEST_ADDNODE -DTEST_DELETENODE -DTEST_CALCULATE 

SRCS = convert.c list.c main.c 
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw14: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw14

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testcase1: hw14
	./hw14 inputs/input1.txt > test
	diff test outputs/expected1.txt > grade.txt

testcase2: hw14
	./hw14 inputs/input2.txt > test
	diff test outputs/expected2.txt > grade.txt


memory: hw14
	$(VAL) ./hw14 inputs/test1

clean: # remove all machine generated files
	rm -f hw14 *.o output?


