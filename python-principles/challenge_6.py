"""
Double letters
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
"""

def double_letters(checkString):
    doubleLetter = False
    a = b = ""
    for letter in range(0, len(checkString)):
        a = checkString[letter]
        if len(checkString)>letter+1:
            b = checkString[letter+1]
            if a == b:
                doubleLetter = True
    return doubleLetter

print(double_letters("Hallo"))