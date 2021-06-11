# ***
# *** DO NOT modify this file 
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_CONVERT -DTEST_READLIST -DTEST_DELETELIST -DTEST_ADDNODE -DTEST_DELETENODE
VALGRIND = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose
SRCS = main.c convert.c list.c
OBJS = $(SRCS:%.c=%.o)

hw13: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw14

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: hw14
	for case in 1 2 3 4 5; do \
	./hw14 inputs/test$$case > output$$case; \
	diff output$$case expected/expected$$case; \
	done

test1: hw14
	./hw14 inputs/test2 > output1
	diff output1 expected/expected2



memory: hw14
	for case in 1 2 3 4 5; do \
	echo "################################"; \
	echo test$$case;\
	$(VALGRIND) ./hw14 inputs/test$$case > output$$case; \
	tail -10 vallog; \
	done


clean: # remove all machine generated files
	rm -f hw14 *.o output?


