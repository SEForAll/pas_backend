

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 
VAL = valgrind --leak-check=yes --leak-check=full --show-leak-kinds=all

SRCS = main.c 
OBJS = $(SRCS:%.c=%.o)

hw21: $(OBJS) 
	$(GCC) $(OBJS) -o hw21

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testmemory: hw21
	$(VAL) ./hw21 inputs/test6 

testall: test1 test2 test3 

test0: hw21
	./hw21 inputs/test1

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

clean: # remove all machine generated files
	rm -f hw21 *.o output?


