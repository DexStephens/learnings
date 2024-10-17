# Given two strings, check if one is a permutation of the other

def isPermutation(str1, str2):
    map = {}

    for char in str1:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1
    
    for char in str2:
        if char in map and map[char] > 0:
            if map[char] == 1:
                del map[char]
            else:
                map[char] -= 1
        else:
            return False
    
    return len(map.keys()) == 0


print(isPermutation("testing", "gnitset"))
print(isPermutation("test", "tes"))
print(isPermutation("", "tes"))