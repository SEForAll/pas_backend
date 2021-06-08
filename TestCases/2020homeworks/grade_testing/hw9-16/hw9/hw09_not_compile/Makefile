WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR)

TESTFALGS = -DTEST_MAIN -DDEBUG -DTEST_READDATA -DTEST_WRITEDATA -DTEST_MERGE -DTEST_MERGESSORT -DDEBUG

SRCS = main.c hw09.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw09: $(OBJS)
	$(GCC) $(TESTFALGS) $(OBJS) -o hw09

.c.o:
	$(GCC) $(TESTFALGS) -c $*.c

test1: hw09
	./hw09 inputs/input1 > outputs/output1
	diff outputs/output1 expected/expected1 > grade.txt

test2: hw09
	./hw09 inputs/input2 > outputs/output2
	diff outputs/output2 expected/expected2 > grade.txt

test3: hw09
	./hw09 inputs/input3 > outputs/output3
	diff outputs/output3 expected/expected3 > grade.txt

test4: hw09
	./hw09 inputs/input4 > outputs/output4
	diff outputs/output4 expected/expected4 > grade.txt

test5: hw09
	./hw09 inputs/input5 > outputs/output5
	diff outputs/output5 expected/expected5 > grade.txt

clean: # remove all machine generated files
	rm -f hw09 *.o output?
