

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 
VAL = valgrind --leak-check=yes --leak-check=full --show-leak-kinds=all

SRCS = main.c 
OBJS = $(SRCS:%.c=%.o)

hw21: $(OBJS) 
	$(GCC) $(OBJS) -o hw19

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testmemory: hw19
	$(VAL) ./hw19 inputs/maze6

testall: test1 test2 test3 

test0: hw19
	./hw19 inputs/maze1

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

test6: hw19
	./hw19 inputs/maze6 > output6
	diff output6 expected/expected6

test7: hw19
	./hw19 inputs/maze7 > output7
	diff output7 expected/expected7

test8: hw19
	./hw19 inputs/maze8 > output8
	diff output8 expected/expected8

test9: hw19
	./hw19 inputs/maze9 > output9
	diff output9 expected/expected9

test10: hw19
	./hw19 inputs/maze10 > output10
	diff output10 expected/expected10

test11: hw19
	./hw19 inputs/maze11 > output11
	diff output11 expected/expected11

test12: hw19
	./hw19 inputs/maze12 > output12
	diff output12 expected/expected12

test13: hw19
	./hw19 inputs/maze13 > output13
	diff output13 expected/expected13

clean: # remove all machine generated files
	rm -f hw19 *.o output?


