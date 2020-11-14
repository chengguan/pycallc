"""
    Source: https://www.journaldev.com/31907/calling-c-functions-from-python
"""

from ctypes import *

so_file = './functions.so'

my_function = CDLL(so_file)

print(f"type(my_function) = {type(my_function)}")
print(f"my_function.square(10) = {my_function.square(10)}")

# Create a char array as Python strings are immutable.
# Source: https://stackoverflow.com/questions/26363641/passing-a-pointer-value-to-a-c-function-from-python
pBuf = create_string_buffer(100)

get_string = CDLL(so_file).print_string
get_string.argtypes = [c_int, POINTER(c_char)]
get_string.restype = c_int

print(get_string(120, pBuf))
print(f"This is the string printed: {pBuf.value.decode('utf-8')}")