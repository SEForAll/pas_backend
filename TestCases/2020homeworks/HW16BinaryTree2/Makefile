WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_BUILDTREE -DTEST_PRINTPATH 

SRCS = main.c tree.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose

hw16: $(OBJS)
	$(GCC) $(OBJS) -o hw16

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw16
	./hw16 inputs/test1in inputs/test1post > outputs/output1
	diff -w outputs/output1 expected/expected1

test2: hw16
	./hw16 inputs/test2in inputs/test2post > outputs/output2
	diff -w outputs/output2 expected/expected2

test3: hw16
	./hw16 inputs/test3in inputs/test3post > outputs/output3
	diff -w outputs/output3 expected/expected3

test4: hw16
	./hw16 inputs/test4in inputs/test4post > outputs/output4
	diff -w outputs/output4 expected/expected4

test5: hw16
	./hw16 inputs/test5in inputs/test5post > outputs/output5
	diff -w outputs/output5 expected/expected5

test6: hw16
	./hw16 inputs/test6in inputs/test6post > outputs/output6
	diff -w outputs/output6 expected/expected6

clean: # remove all machine generated files
	rm -f hw16 *.o output?



