# Write a method to replace all spaces in a string with %20. You may assume that the string has 
# sufficient space at the end to hold the additional characters, and that you are given the 
# true length of the string

# Hint: easiest to modify a string by starting from the end and working to the beginning
# Hint: can we just count the spaces in the string

def URLify(str, length):
    str = list(str)
    left = length - 1
    right = len(str) - 1

    while left > 0:
        if str[left] != " ":
            str[right] = str[left]
            right -= 1
        else:
            str[right] = '0'
            str[right - 1] = '2'
            str[right - 2] = '%'

            right -= 3
        left -= 1
    
    return str

print(URLify("Mr John Smith    ", 13))
