#!/usr/bin/env python3

from enum import Enum
from string import ascii_lowercase


class Symbol(Enum):
    BREAK_SIGN = '|'
    MUL_SIGN = '*'
    DIV_SIGN = '/'
    PLUS_SIGN = '+'
    MINUS_SIGN = '-'
    LEFT_BRACKET = '('
    RIGHT_BRACKET = ')'

    # 1 send to lst_RPN
    # 2 push last from stack to lst_RPN
    # 3 remove last from stack and last candidate
    # 4 finish
    # 5 error

class Action(Enum):
    BREAK_SIGN =    {'|':4, '-':1, '+':1, '*':1, '/':1, '(':1, ')':5}
    PLUS_SIGN =     {'|':2, '-':2, '+':2, '*':1, '/':1, '(':1, ')':2}
    MINUS_SIGN =    {'|':2, '-':2, '+':2, '*':1, '/':1, '(':1, ')':2}
    MUL_SIGN =      {'|':2, '-':2, '+':2, '*':2, '/':2, '(':1, ')':2}
    DIV_SIGN =      {'|':2, '-':2, '+':2, '*':2, '/':2, '(':1, ')':2}
    LEFT_BRACKET =  {'|':5, '-':1, '+':1, '*':1, '/':1, '(':1, ')':3}


def brackets_trim(input_data: str) -> str:

    def to_RPN(input_data):
        input_data = input_data + '|'
        lst_RPN = []
        stack = ['|']
        for sym in input_data:
            print(stack)
            if sym in ascii_lowercase:
                print('added char')
                lst_RPN.append(sym)
            else:
                print(stack[-1])
                action_choice = Action[Symbol(sym).name].value[stack[-1]]
                print('-----', action_choice)
                if action_choice == 1:
                    stack.append(sym)
                elif action_choice == 2:
                    last = stack.pop(-1)
                    lst_RPN.append(last)
                elif action_choice == 3:
                    stack.pop(-1)
                elif action_choice == 4:
                    return lst_RPN
                else:
                    return None

    return to_RPN(input_data)

data = 'a+b*c'
data = 'a+c'
print(data)
print(brackets_trim(data))