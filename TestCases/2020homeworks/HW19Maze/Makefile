

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS =   

SRCS = main.c maze.c
OBJS = $(SRCS:%.c=%.o)
VAL = valgrind --tool=memcheck --log-file=memcheck.txt --leak-check=full --verbose

hw19: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw19

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 


test1: hw19
	./hw19 inputs/maze1 > outputs/output1
	diff outputs/output1 expected/expected1 > grade.txt

test2: hw19
	./hw19 inputs/maze2 > outputs/output2
	diff outputs/output2 expected/expected2 > grade.txt

test3: hw19
	./hw19 inputs/maze3 > outputs/output3
	diff outputs/output3 expected/expected3 > grade.txt

test4: hw19
	./hw19 inputs/maze4 > outputs/output4
	diff outputs/output4 expected/expected4 > grade.txt

test5: hw19
	./hw19 inputs/maze5 > outputs/output5
	diff outputs/output5 expected/expected5 > grade.txt

test6: hw19
	./hw19 inputs/maze6 > outputs/output6
	diff outputs/output6 expected/expected6 > grade.txt

test7: hw19
	./hw19 inputs/maze7 > outputs/output7
	diff outputs/output7 expected/expected7 > grade.txt

test8: hw19
	./hw19 inputs/maze8 > outputs/output8
	diff outputs/output8 expected/expected8 > grade.txt

test9: hw19
	./hw19 inputs/maze9 > outputs/output9
	diff ooutputs/utput9 expected/expected9 > grade.txt

test10: hw19
	./hw19 inputs/maze10 > outputs/output10
	diff outputs/output10 expected/expected10 > grade.txt

test11: hw19
	./hw19 inputs/maze11 > outputs/output11
	diff outputs/output11 expected/expected11 > grade.txt

test12: hw19
	./hw19 inputs/maze12 > outputs/output12
	diff outputs/output12 expected/expected12 > grade.txt

test13: hw19
	./hw19 inputs/maze13 > outputs/output13
	diff outputs/output13 expected/expected13 > grade.txt

clean: # remove all machine generated files
	rm -f hw19 *.o output?


