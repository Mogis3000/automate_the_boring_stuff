# Automate the Boring Stuff by Al Sweigart
# pg 49

from ast import AsyncFunctionDef
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')