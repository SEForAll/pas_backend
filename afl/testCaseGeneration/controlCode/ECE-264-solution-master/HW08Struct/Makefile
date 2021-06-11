# ***
# *** DO NOT modify this file
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror 
GCC = gcc -std=c99 -g $(WARNING) $(ERROR)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

TESTFALGS = -DTEST_MAIN -DTEST_COUNTVECTOR -DTEST_READVECTOR -DTEST_COMPAREVECTOR -DTEST_WRITEVECTOR

VALGRIND = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose

SRCS = main.c hw08.c
OBJS = $(SRCS:%.c=%.o)

hw08: $(OBJS)
	$(GCC) $(TESTFALGS) $(OBJS) -o hw08

.c.o:
	$(GCC) $(TESTFALGS) -c $*.c


testall: hw08
	for case in 1 2 3 4 5; do \
	./hw08 inputs/test$$case.bin output$$case; \
	diff output$$case expected/expected$$case.bin; \
	done
test1: hw08
	./hw08 inputs/test1.bin output1
	#diff output1 expected/expected1.bin
	
memleak: hw08
	for case in 1 2 3 4 5; do \
	echo "################################"; \
	echo testcase $$case; \
	$(VALGRIND) ./hw08 inputs/test$$case.bin output$$case; \
	tail -10 vallog; \
	done
	

clean: # remove all machine generated files
	rm -f hw08 *.o output?
