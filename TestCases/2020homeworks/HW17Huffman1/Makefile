

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 


TESTFALGS = -DTEST_BUILDTREE -DTEST_PRINTPATH 

SRCS = main.c tree.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw17: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw17

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 


test1: hw17
	./hw17 inputs/input1 | sort > outputs/output1
	diff outputs/output1 expected/expected1 > grade.txt

test2: hw17
	./hw17 inputs/input2 | sort > outputs/output2
	diff outputs/output2 expected/expected2 > grade.txt

test3: hw17
	./hw17 inputs/input3 | sort > outputs/output3
	diff outputs/output3 expected/expected3 > grade.txt

test4: hw17
	./hw17 inputs/input4 | sort > outputs/output4
	diff outputs/output4 expected/expected4 > grade.txt

test5: hw17
	./hw17 inputs/input5 | sort > outputs/output5
	diff outputs/output5 expected/expected5 > grade.txt


clean: # remove all machine generated files
	rm -f hw17 *.o output?

