# ***
# *** DO NOT modify this file 
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 
VALGRIND = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose
TESTFALGS = -DTEST_DIVIDE -DTEST_INTERLEAVE -DTEST_SHUFFLE

SRCS = main.c shuffle.c
OBJS = $(SRCS:%.c=%.o)

hw10: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw12

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: test1 test2 test3 test4 test5 test6 test7 test8 test9 test10

test1: hw12
	./hw12 3 1 | sort > output1
	diff -w output1 expected/expected31

test2: hw12
	./hw12 3 2 | sort > output2
	diff -w output2 expected/expected32

test3: hw12
	./hw12 4 2 | sort > output3
	diff -w output3 expected/expected42

test4: hw12
	./hw12 4 3 | sort | uniq > output4
	diff -w output4 expected/expected_4_3
test5: hw12
	./hw12 4 5 | sort | uniq > output5
	diff -w output5 expected/expected_4_5

test6: hw12
	./hw12 5 2 | sort | uniq > output6
	diff -w output6 expected/expected_5_2

test7: hw12
	./hw12 6 2 | sort | uniq  > output7
	diff -w output7 expected/expected_6_2
test8: hw12
	./hw12 7 3 | sort | uniq  > output8
	diff -w output8 expected/expected_7_3
test9: hw12
	./hw12 8 2 | sort | uniq  > output9
	diff -w output9 expected/expected_8_2
test10: hw12
	./hw12 11 2 | sort | uniq  > output10
	diff -w output10 expected/expected_11_2

memory: hw12
	$(VALGRIND) ./hw12 11 2 > o1
	tail -10 vallog
	$(VALGRIND) ./hw12 8 2 > o1
	tail -10 vallog
	$(VALGRIND) ./hw12 7 3 > o1
	tail -10 vallog

clean: # remove all machine generated files
	rm -f hw12 *.o output?


