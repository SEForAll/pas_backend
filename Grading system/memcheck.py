import re

# file --> a file that has all the valgrind information on it (not verbose)
# returns how many bytes are in use and in how many blocks at the end of the program
def memcheck(file):
    text = file.read()

    p = re.compile(r'in use at exit: (\d+) bytes in (\d+) blocks')

    bytesInUse = int(p.search(text).group(1))
    blocks = int(p.search(text).group(2))

    return bytesInUse, blocks
