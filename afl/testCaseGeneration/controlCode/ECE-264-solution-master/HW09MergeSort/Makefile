# ***
# *** DO NOT modify this file
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror 
GCC = gcc -std=c99 -g $(WARNING) $(ERROR)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

TESTFALGS = -DTEST_MAIN -DTEST_READDATA -DTEST_MERGE -DTEST_MERGESSORT -DTEST_WRITEDATA

VALGRIND = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose

SRCS = main.c hw09.c
SRCS_TEST = testgen.c hw09.c
OBJS = $(SRCS:%.c=%.o)

hw09: $(OBJS)
	$(GCC) $(TESTFALGS) $(OBJS) -o hw09
	
testgen: $(OBJS)
	$(GCC) $(TESTFALGS) $(OBJS) -o testgen

.c.o:
	$(GCC) $(TESTFALGS) -c $*.c

testgenall: testgen
	for case in 1 ; do \
	./testgen testgen$$case; \
	done 
testall: hw09
	for case in 1 2 3 4 5 6; do \
	./hw09 inputs/input$$case output$$case; \
	diff output$$case expected/expected$$case; \
	done
test6: hw09
	./hw09 inputs/input6 output1
	diff output1 expected/expected6
	
memleak: hw09
	for case in 1 2 3 4 5 6; do \
	echo "################################"; \
	echo testcase $$case; \
	$(VALGRIND) ./hw09 inputs/input$$case output$$case; \
	tail -10 vallog; \
	done
	

clean: # remove all machine generated files
	rm -f hw09 *.o output?
