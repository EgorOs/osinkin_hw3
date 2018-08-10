#!/usr/bin/env python3

from enum import Enum
from string import ascii_lowercase




def brackets_trim(input_data: str) -> str:
 
    # TOKEN = set(ascii_lowercase)
    # OPERATOR = {'+', '-', '*', '/'}
    # BRACKET = {'(', ')'}

    def get_symbol_priority(sym):
        symbol_priority = {('+', '-'):1, ('*', '/'):2, ('(', ')'):3}
        for key in symbol_priority.keys():
            if sym in key:
                return symbol_priority[key]

    lst_RPN = []
    steck = [] # dont forget to clear
    last_priority = 0
    for sym in input_data:
        if sym in ascii_lowercase:
            lst_RPN.append(sym)
        else:
            priority = get_symbol_priority(sym)
            if priority > last_priority:
                steck.append(sym)
            elif priority == last_priority:
                lst_RPN += steck[::-1]
                steck = []
                steck.append(sym)
            else:
                lst_RPN.append(sym)
            last_priority = priority


    
    return lst_RPN+steck[::-1]

data = 'a/b*c'
print(data)
print(brackets_trim(data))