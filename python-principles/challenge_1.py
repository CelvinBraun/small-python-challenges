"""
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

def capital_indexes(capitalString):
    indexList = []
    for element in range(0, len(capitalString)):
        if capitalString[element].isupper() == True:
            indexList.append(element)

    return indexList


indexValues = capital_indexes("HeLlO")
print(indexValues)