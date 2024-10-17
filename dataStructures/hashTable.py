class HashTable:
    def __init__(self):
        pass

    def hash(self,  key):
        return hash(key)
    

# Create the hash table with a length, place the hash based on a modulo of the current length
# Each index has a value of a linked list where we can look for the exact key