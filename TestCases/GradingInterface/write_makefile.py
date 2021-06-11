import os


def write_makefile(path, warnings, errors, srcs, name='no_name'):
    make = ''

    make += f'WARNING = {warnings}\n'
    make += f'ERROR = {errors}\n'
    make += 'GCC = gcc -std=c99 -g $(WARNING) $(ERROR)\n\n'

    make += f'SRCS = {srcs}\n'
    make += 'OBJS = $(SRCS:%.c=%.o)'

    make += f'{name}: $(OBJS)\n'
    make += '\t$(GCC) $(TESTFALGS) $(OBJS) -o sort\n\n'

    make += '.c.o: \n\t$(GCC) $(TESTFALGS) -c $*.c\n\n'

    os.chdir(path)

    if os.path.isdir(f'{path}/inputs') is False or os.path.isdir(f'{path}/expected') is False:
        return -1

    inputs = os.listdir(f'{path}/inputs')
    expected = os.listdir(f'{path}/expected')

    inputs.sort()
    expected.sort()

    for files in [inputs, expected]:
        for filename in files:
            if filename.endswith('.txt') is False:
                files.remove(filename)

    if len(inputs) != len(expected):
        return -1

    for i in range(len(inputs)):
        make += f'test{i + 1}: {name}\n\t./{name} inputs/{inputs[i]} > output{i + 1}\n\tdiff output{i + 1} expected/{expected[i]} > grade.txt\n\n'

    make += 'clean: \n\trm -f sort *.o output?'

    with open('Makefile', 'w+') as f:
        f.write(make)

    return 0


if __name__ == '__main__':
    path = '/Users/alexgieson/test/'
    warnings = '-Wall -Wshadow --pedantic'
    errors = '-Wvla -Werror'
    sources = 'main.c sort.c'

    write_makefile(path, warnings, errors, sources, name='myfiles')

    os.chdir(path)

    os.system('diff inputs/one.txt expected/one.txt > grade.txt')
