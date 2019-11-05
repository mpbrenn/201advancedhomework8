#!/usr/bin/env python3

#testing travis again

#test again

import readline
from termcolor import colored, cprint
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = colored(function(arg1, arg2), 'red')
            stack.append(result)
        
        #print(stack)
    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()


def main():
    while True:
        userInput = input("rpn calc> ")
        cprint(userInput, 'green')
        result = calculate(userInput)
        print(result)

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
