WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 
VAL = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose
TESTFALGS = -DTEST_BUILDTREE -DTEST_PRINTPATH 

SRCS = main.c maze.c
OBJS = $(SRCS:%.c=%.o)

hw21: $(OBJS)
	$(GCC) $(OBJS) -o hw21

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: hw21
	for case in 1 2 3 4 5 6; do \
	./hw21 inputs/test$$case > output$$case; \
	diff output$$case expected/expected$$case; \
	done

test1: hw21
	./hw21 inputs/test1 > output1
	diff output1 expected/expected1

test2: hw21
	./hw21 inputs/test2 > output2
	diff output2 expected/expected2

test3: hw21
	./hw21 inputs/test3 > output3
	diff output3 expected/expected3

test4: hw21
	./hw21 inputs/test4 > output4
	diff output4 expected/expected4

test5: hw21
	./hw21 inputs/test5 > output5
	diff output5 expected/expected5
	
test6: hw21
	./hw21 inputs/test6 > output6
	diff output6 expected/expected6

memory: hw21
	for case in 1 2 3 4 5 6; do \
	echo "################################"; \
	echo test$$case;\
	$(VAL) ./hw21 inputs/test$$case > output$$case; \
	tail -10 vallog; \
	done

clean: # remove all machine generated files
	rm -f hw21 *.o output?* vallog testgen