from distutils.ccompiler import new_compiler

inputfilename = '/home/tony/research/test.c'    # student submission path in database

compiler = new_compiler()
try:
    compiler.compile([inputfilename])
    compiler.link_executable(['test.o'], 'test')
    print("True1")   # Need change later
except:
    print("False1")  # Need change later
    # Remember to set total grade to 0
