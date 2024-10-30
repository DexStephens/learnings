# DESCRIPTION: Given a string, check to see if it is a permutation of a palindrome. Palindrome is the same forwards
# as it is backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words. Ignore casing and non-letter characters
# INPUT: Tact coa
# OUTPUT: Yes, (taco cat, atco cta, etc.)

def palindromePermutation(str):
    # Each character must appear an even number of times, allowing for one odd number
    str = str.lower()

    map = {}
    singleOdd = False

    for char in str:
        if char.isalpha():
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
    
    for key in map:
        if map[key] % 2 != 0:
            if singleOdd == True:
                return False
            else:
                singleOdd = True
    
    return True
    


print(palindromePermutation("Tact coa"))
print(palindromePermutation("testing"))
print(palindromePermutation("mam"))
print(palindromePermutation("mmmdd"))

# NEEDSWORK: how to solve this with a bit vectos?