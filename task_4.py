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


class Action(Enum):
    BREAK_SIGN    = {'|': 4, '-': 1, '+': 1, '*': 1, '/': 1, '(': 1, ')': 5}
    PLUS_SIGN     = {'|': 2, '-': 2, '+': 2, '*': 1, '/': 1, '(': 1, ')': 2}
    MINUS_SIGN    = {'|': 2, '-': 2, '+': 2, '*': 1, '/': 1, '(': 1, ')': 2}
    MUL_SIGN      = {'|': 2, '-': 2, '+': 2, '*': 2, '/': 2, '(': 1, ')': 2}
    DIV_SIGN      = {'|': 2, '-': 2, '+': 2, '*': 2, '/': 2, '(': 1, ')': 2}
    LEFT_BRACKET  = {'|': 5, '-': 1, '+': 1, '*': 1, '/': 1, '(': 1, ')': 3}


def brackets_trim(input_data: str) -> str:
    """Removes extra brackets from expression"""

    def to_postfix(input_data: str) -> str:
        """Implementation of E.W. Dejkstra
        algorithm https://habr.com/post/100869/"""
        input_data = input_data + '|'
        lst_postfix = []
        stack = ['|']
        pos = 0
        while True:
            sym = input_data[pos]
            if sym in set(ascii_lowercase):
                lst_postfix.append(sym)
                pos += 1
            else:
                LAST_SIGN = Symbol(stack[-1]).name
                action_choice = Action[LAST_SIGN].value[sym]
                if action_choice == 1:
                    stack.append(sym)
                    pos += 1
                elif action_choice == 2:
                    last = stack.pop(-1)
                    lst_postfix.append(last)
                elif action_choice == 3:
                    stack.pop(-1)
                    pos += 1
                elif action_choice == 4:
                    break
                else:
                    raise Exception('invalid input string')
        return ''.join(lst_postfix)

    def to_infix(input_data: str) -> str:
        """Postfix to infix algorithm described on
        http://scanftree.com/Data_Structure/postfix-to-infix"""
        stack = []
        sign_priority = {'-':1, '+':1, '*':2, '/':2}
        prev_sign_priority = 1
        for sym in input_data:
            if sym in set(ascii_lowercase):
                stack.append(sym)
            else:
                s1, s2 = stack.pop(-2), stack.pop(-1)
                if prev_sign_priority < sign_priority[sym]:
                    if len(s1) > 1 and '(' not in s1:
                        s1 = '(' + s1 + ')'
                    if len(s2) > 1 and '(' not in s2:
                        s2 = '(' + s2 + ')'
                    stack.append(s1 + sym + s2)
                else:
                    stack.append(s1 + sym + s2)
                prev_sign_priority = sign_priority[sym]
        return stack[0]

    # Remove spaces
    input_data = input_data.replace(' ','')
    return to_infix(to_postfix(input_data))

# data = 'a+b*c'
# data = 'a+b*c+k'
# data = 'a+(b-c)'
# data = 'a+c'
# data = '((a+b*c+k/m))*l'
# data = '(((a+b-c)*((d-e))/(f-g+h)))'
# data = '(a*(b/c)+((d-f)/k))'
# data = 'a'
# data = 'a+ (b+c)'

# print(data)
# print(brackets_trim(data))
