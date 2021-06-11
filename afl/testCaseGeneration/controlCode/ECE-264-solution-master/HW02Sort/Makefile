# ***
# *** You can modify this file. You do not (should not) submit this file
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_SWAP -DTEST_SORT

SRCS = main.c sort.c
OBJS = $(SRCS:%.c=%.o)

VALGRIND = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose

sort: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o sort

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: test1 test2 test3 test4

test1: sort
	./sort inputs/test1 > output1
	diff output1 expected/expected1

test2: sort
	./sort inputs/test2 > output2
	diff output2 expected/expected2

test3: sort
	./sort inputs/test3 > output3
	diff output3 expected/expected3

test4: sort
	./sort inputs/test4 > output4
	diff output4 expected/expected4

testfor: sort  # same as testall
	for case in 1 2 3 4 5; do \
	echo $$case; \
	./sort inputs/test$$case > output$$case; \
	diff output$$case expected/expected$$case; \
	done
	
memleak: sort
	for case in 1 2 3 4 5; do \
	echo "################################"; \
	echo testcase $$case; \
	$(VALGRIND) ./sort inputs/test$$case &> /dev/null; \
	tail -10 vallog; \
	done

clean: # remove all machine generated files
	rm -f sort *.o output?


