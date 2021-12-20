"""
Type check
Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
"""

def only_ints(value_a, value_b):
    if type(value_a)==int and type(value_b)==int:
        return True
    else:
        return False

print(only_ints(1,True))