# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:43:19 2020

@author: sreevalli kurla ksv
"""
######    FUNCTIONS

#     type dir(__builtins__) in console to know all the builtin functions
dir(__builtins__)
# OUTPUT
# ['ArithmeticError',
#  'AssertionError',
#  'AttributeError',
#  'BaseException',
#  'BlockingIOError',
#  'BrokenPipeError',
#  'BufferError',
#  'BytesWarning',
#  'ChildProcessError',
#  'ConnectionAbortedError',
#  'ConnectionError',
#  'ConnectionRefusedError',
#  'ConnectionResetError',
#  'DeprecationWarning',
#  'EOFError',
#  'Ellipsis',
#  'EnvironmentError',
#  'Exception',
#  'False',
#  'FileExistsError',
#  'FileNotFoundError',
#  'FloatingPointError',
#  'FutureWarning',
#  'GeneratorExit',
#  'IOError',
#  'ImportError',
#  'ImportWarning',
#  'IndentationError',
#  'IndexError',
#  'InterruptedError',
#  'IsADirectoryError',
#  'KeyError',
#  'KeyboardInterrupt',
#  'LookupError',
#  'MemoryError',
#  'ModuleNotFoundError',
#  'NameError',
#  'None',
#  'NotADirectoryError',
#  'NotImplemented',
#  'NotImplementedError',
#  'OSError',
#  'OverflowError',
#  'PendingDeprecationWarning',
#  'PermissionError',
#  'ProcessLookupError',
#  'RecursionError',
#  'ReferenceError',
#  'ResourceWarning',
#  'RuntimeError',
#  'RuntimeWarning',
#  'StopAsyncIteration',
#  'StopIteration',
#  'SyntaxError',
#  'SyntaxWarning',
#  'SystemError',
#  'SystemExit',
#  'TabError',
#  'TimeoutError',
#  'True',
#  'TypeError',
#  'UnboundLocalError',
#  'UnicodeDecodeError',
#  'UnicodeEncodeError',
#  'UnicodeError',
#  'UnicodeTranslateError',
#  'UnicodeWarning',
#  'UserWarning',
#  'ValueError',
#  'Warning',
#  'WindowsError',
#  'ZeroDivisionError',
#  '__IPYTHON__',
#  '__build_class__',
#  '__debug__',
#  '__doc__',
#  '__import__',
#  '__loader__',
#  '__name__',
#  '__package__',
#  '__spec__',
#  'abs',
#  'all',
#  'any',
#  'ascii',
#  'bin',
#  'bool',
#  'breakpoint',
#  'bytearray',
#  'bytes',
#  'callable',
#  'cell_count',
#  'chr',
#  'classmethod',
#  'compile',
#  'complex',
#  'copyright',
#  'credits',
#  'debugcell',
#  'debugfile',
#  'delattr',
#  'dict',
#  'dir',
#  'display',
#  'divmod',
#  'enumerate',
#  'eval',
#  'exec',
#  'filter',
#  'float',
#  'format',
#  'frozenset',
#  'get_ipython',
#  'getattr',
#  'globals',
#  'hasattr',
#  'hash',
#  'help',
#  'hex',
#  'id',
#  'input',
#  'int',
#  'isinstance',
#  'issubclass',
#  'iter',
#  'len',
#  'license',
#  'list',
#  'locals',
#  'map',
#  'max',
#  'memoryview',
#  'min',
#  'next',
#  'object',
#  'oct',
#  'open',
#  'ord',
#  'pow',
#  'print',
#  'property',
#  'range',
#  'repr',
#  'reversed',
#  'round',
#  'runcell',
#  'runfile',
#  'set',
#  'setattr',
#  'slice',
#  'sorted',
#  'staticmethod',
#  'str',
#  'sum',
#  'super',
#  'tuple',
#  'type',
#  'vars',
#  'zip']

######
#-------------THERE ARE CONVERSION FUNCTIONS


######    working with a few functions
# peint()
# len()
name= "python"
print(len(name))

alist= [10,20,30]
print(len(alist))

adict={"chap1":12,"chap2":23}
print(len(adict))

# input()
name=input("enter any name:")
print("you entered:", name)

# id() : identify some unique reference
val = 10
info= [102,567]
print(id(val))
print(id(info))

# range()
print(list(range(1,11)))
print(list(range(2,20,2)))
print(tuple(range(1,20,2)))

# type()
print(type(val))
print(type(info))

# isinstance()
print(isinstance(val,list))
print(isinstance(val,int))
print(isinstance(info,str))

# max() min() sum()
print(max(info))
print(min(info))
print(sum(info))

# oct,float,hex  values for an integer
val= 100
print(oct(val))
print(float(val))
print(hex(val))

####   CHANGING TUPLE TO LIST AND BACK, TO MODIFY ANY INDEX OR VALUE, as we can't change any value in tuple.

atup=(10,20,30)
alist= list(atup)
alist[1]= 40
atup = tuple(alist)
print("after modifying:", atup)



#########        STATEMENTS



# if  if- elif-elif-elif-..........else

a= 10
b=20

if a<b:
    print("A is lessthan B")
    #print("inside if only")
    
# if-else

a= 190
b=20

if a<b:
    print("A is lessthan B")
else:
    print("b is lessthan a")

# if- elif-elif-elif-..........else
name=input("enter any name:")
if name.isupper():
    print("name is uppercase")
elif name.islower():
    print("name is lowercase")

val=10
if isinstance(val,int):
    print("object is type int")
else:
    print("object is someother type")

color= input("enter any color:")
if color=="red":
    print("RED")
elif color=="green":
    print("GREEN")
elif color=="blue":
    print("BLUE")
elif color=="black":
    print("BLACK")
else:
    print("unknown color")





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
