from temp.module import greet2, greet

# __pycache__ is a special directory that Python creates to store compiled bytecode files of your .py source files.

'''
Python compiles your code to bytecode before execution for better performance.
Instead of compiling the .py file every time your program runs, Python saves the
compiled version in the __pycache__ folder to speed up future executions.
'''

print('g:', greet())
print('g:', greet2())