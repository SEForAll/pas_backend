WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

TESTFALGS = -DTEST_FUNCTIONS -DTEST_COUNTVECTOR -DTEST_READVECTOR -DTEST_COMPAREVECTOR -DTEST_WRITEVECTOR -DTEST_MAIN

SRCS = hw08.c main.c
OBJS = $(SRCS:%.c=%.o)


hw08: $(OBJS)
	$(GCC) $(TESTFALGS) $(OBJS) -o hw08

.c.o:
	$(GCC) $(TESTFALGS) -c $*.c

testmemory: hw08
	$(VAL) ./hw08 inputs/test3.bin output3

testall: test1 test2 test3 test4 test5

test1: hw08
	./hw08 inputs/test1.bin output1
	diff output1 expected/expected1.bin

test2: hw08
	./hw08 inputs/test2.bin output2
	diff output2 expected/expected2.bin

test3: hw08
	./hw08 inputs/test3.bin output3
	diff output3 expected/expected3.bin

test4: hw08
	./hw08 inputs/test4.bin output4
	diff output4 expected/expected4.bin

test5: hw08
	./hw08 inputs/test5.bin output4
	diff output4 expected/expected5.bin

clean:
	rm -f hw08 *.o output?
