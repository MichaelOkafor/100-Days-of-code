# Slicing list and tuples

piano_keys = ["a", "b", "c", "d", "e", "f", "g", "h"]
# gets the list from the 2nd to the fifth
print(piano_keys[2:5])
# Gets the letters from the 2nd to the last
print(piano_keys[2:])
# gets the letters in the list to the fifth one
print(piano_keys[:5])
# goes through the list from the 2nd to the 6th and omits one
print(piano_keys[2:6:2])
# scans through the list and skips two
print(piano_keys[::2])
# reversing a list
print(piano_keys[::-1])
