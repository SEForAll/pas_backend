

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 


TESTFALGS = 

SRCS = 
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw18: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw18

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 


test1: hw18
	./hw18 inputs/test1 > outputs/output1
	diff outputs/output1 expected/expected1 > grade.txt

test2: hw18
	./hw18 inputs/test2 > outputs/output2
	diff outputs/output2 expected/expected2 > grade.txt

test3: hw18
	./hw18 inputs/test3 > outputs/output3
	diff outputs/output3 expected/expected3 > grade.txt

test4: hw18
	./hw18 inputs/test4 > outputs/output4
	diff outputs/output4 expected/expected4 > grade.txt

test5: hw18
	./hw18 inputs/test5 > outputs/output5
	diff outputs/output5 expected/expected5 > grade.txt


clean: # remove all machine generated files
	rm -f hw18 *.o output?

