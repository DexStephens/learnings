# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
def isUniqueWithHashmap(str):
    map = {}

    for char in str:
        if char in map:
            return False
        else:
            map[char] = True
    
    return True

def isUniqueWithBitVector(str):
    pass

def isUniqueWithSorting(str):
    # Need to do a quick sort here
    last = ""

    for char in str:
        if char == last:
            return False
        else:
            last = char
    
    return True



string1 = "testing"
string2 = "tesing"

print(isUniqueWithHashmap(string1))
print(isUniqueWithHashmap(string2))