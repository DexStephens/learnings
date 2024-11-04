# DESCRIPTION: Implement a method to perform basic string compression using the counts of repeated characters.
# If the compressed string would not become smaller than the original string, return the original string. 
# Assume uppercase and lowercase letters
# INPUT: aabcccccaaa -> a2b1c5a3

def stringCompression(str):
    if len(str) == 0:
        return str
    
    count = 1
    prev = str[0]
    output = []

    for i in range(1, len(str)):
        current = str[i]

        if current != prev:
            output.append(f'{prev}{count}')
            prev = current
            count = 1
        else:
            count += 1
    
    output.append(f'{prev}{count}')

    final = ''.join(output)

    print(final)

    if len(final) < len(str):
        return final
    else:
        return str




print(stringCompression("aabcccccaaa"))