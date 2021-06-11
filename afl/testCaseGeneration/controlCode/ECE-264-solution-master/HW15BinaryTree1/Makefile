# ***
# *** DO NOT modify this file 
# ***

WARNING = -Wall -Wshadow --pedantic
ERROR = -Wvla -Werror
GCC = gcc -std=c99 -g $(WARNING) $(ERROR) 

TESTFALGS = -DTEST_BUILDTREE 
VALGRIND = valgrind --tool=memcheck --log-file=vallog --leak-check=full --verbose
SRCS = main.c tree.c
OBJS = $(SRCS:%.c=%.o)

hw15: $(OBJS) 
	$(GCC) $(TESTFALGS) $(OBJS) -o hw15

.c.o: 
	$(GCC) $(TESTFALGS) -c $*.c 

testall: hw15
	for case in 1 2 3 4 6; do \
	./hw15 "inputs/test$${case}in" "inputs/test$${case}post" "output$${case}"; \
	diff "output$${case}" "expected/expected$${case}"; \
	done

test1: hw15
	./hw15 inputs/test1in inputs/test1post output1



memory: hw15
	for case in 1 2 3 4 5 6; do \
	echo "################################"; \
	echo test$$case;\
	$(VALGRIND) ./hw15 inputs/test($$case)in inputs/test($$case)post output$$case; \
	tail -10 vallog; \
	done


clean: # remove all machine generated files
	rm -f hw15 *.o output?


