# ***
# *** DO NOT modify this file 
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_CALCULATE -DTEST_READLIST -DTEST_DELETELIST -DTEST_ADDNODE -DTEST_DELETENODE
VALGRIND = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose
SRCS = main.c calculate.c list.c
OBJS = $(SRCS:%.c=%.o)

hw13: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw13

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: hw13
	for case in 1 2 3 4 5 6; do \
	./hw13 inputs/test$$case > output$$case; \
	diff output$$case expected/expected$$case; \
	done

test1: hw13
	./hw11 inputs/test1 output1
	diff output1 expected/expected1



memory: hw13
	for case in 1 2 3 4 5 6; do \
	echo "################################"; \
	echo test$$case;\
	$(VALGRIND) ./hw13 inputs/test$$case > output$$case; \
	tail -10 vallog; \
	done


clean: # remove all machine generated files
	rm -f hw13 *.o output?


