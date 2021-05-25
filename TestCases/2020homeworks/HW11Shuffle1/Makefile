WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_DIVIDE -DTEST_INTERLEAVE -DTEST_SHUFFLE

SRCS = main.c shuffle.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw11: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw11

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw11
	./hw11 4 | sort > outputs/output1
	diff -w outputs/output1 expected/expected4 > grade.txt

test2: hw11
	./hw11 8 | sort > outputs/output2
	diff -w outputs/output2 expected/expected8 > grade.txt

test3: hw11
	./hw11 11 | sort > outputs/output3
	diff -w outputs/output3 expected/expected11 > grade.txt

clean: # remove all machine generated files
	rm -f hw11 *.o output?


