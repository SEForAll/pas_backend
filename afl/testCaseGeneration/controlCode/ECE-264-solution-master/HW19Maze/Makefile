WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 
VAL = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose
TESTFALGS = -DTEST_BUILDTREE -DTEST_PRINTPATH 

SRCS = main.c maze.c
OBJS = $(SRCS:%.c=%.o)

hw19: $(OBJS)
	$(GCC) $(OBJS) -o hw19

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: hw19
	for case in 1 2 3 4 5 6 7 8 9 10 11 12 13; do \
	./hw19 inputs/maze$$case > output$$case; \
	diff output$$case expected/expected$$case; \
	done

test1: hw19
	./hw19 inputs/maze1 > output1
	diff output1 expected/expected1

test2: hw19
	./hw19 inputs/maze2 > output2
	diff output2 expected/expected2

test3: hw19
	./hw19 inputs/maze3 > output3
	diff output3 expected/expected3

test4: hw19
	./hw19 inputs/maze4 > output4
	diff output4 expected/expected4

test5: hw19
	./hw19 inputs/maze5 > output5
	diff output5 expected/expected5
	
test13: hw19
	./hw19 inputs/maze13 > output13
	diff output13 expected/expected13

memory: hw19
	for case in 1 2 3 4 5 6 7 8 9 10 11 12 13; do \
	echo "################################"; \
	echo test$$case;\
	$(VAL) ./hw19 inputs/maze$$case > output$$case; \
	tail -10 vallog; \
	done

clean: # remove all machine generated files
	rm -f hw19 *.o output?* vallog testgen