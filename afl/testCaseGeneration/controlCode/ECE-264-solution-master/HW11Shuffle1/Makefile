# ***
# *** DO NOT modify this file 
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_DIVIDE -DTEST_INTERLEAVE -DTEST_SHUFFLE
VALGRIND = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose
SRCS = main.c shuffle.c
OBJS = $(SRCS:%.c=%.o)

hw10: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw11

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: test1 test2 test3

test1: hw11
	./hw11 4 | sort > output4
	diff -w output4 expected/expected4

test2: hw11
	./hw11 8 | sort > output8
	diff -w output8 expected/expected8

test3: hw11
	./hw11 11 | sort > output11
	diff -w output11 expected/expected11

memory: hw11
	$(VALGRIND) ./hw11 4 > o1
	tail -10 vallog
	$(VALGRIND) ./hw11 8 > o1
	tail -10 vallog
	$(VALGRIND) ./hw11 11 > o1
	tail -10 vallog


clean: # remove all machine generated files
	rm -f hw11 *.o output?


