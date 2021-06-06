WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_BUILDTREE

SRCS = main.c tree.c
OBJS = $(SRCS:%.c=%.o)

hw15: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw15

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

test1: hw15
	./hw15 inputs/test1in inputs/test1post outputs/output1
	diff outputs/output1 expected/expected1 > grade.txt

test2: hw15
	./hw15 inputs/test2in inputs/test2post outputs/output2
	diff outputs/output2 expected/expected2 > grade.txt

test3: hw15
	./hw15 inputs/test3in inputs/test3post outputs/output3
	diff outputs/output3 expected/expected3 > grade.txt

test4: hw15
	./hw15 inputs/test4in inputs/test4post outputs/output4
	diff outputs/output4 expected/expected4 > grade.txt

test5: hw15
	./hw15 inputs/test5in inputs/test5post outputs/output5
	diff outputs/output5 expected/expected5 > grade.txt

test6: hw15
	./hw15 inputs/test6in inputs/test6post outputs/output6
	diff outputs/output6 expected/expected6 > grade.txt

clean: # remove all machine generated files
	rm -f hw15 *.o output?


