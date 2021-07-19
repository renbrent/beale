"""
Title: decipher.py
Created: Brent Basiano
Description: This program takes a key to decipher a beale cipher.
The beale cipher is a coded message that shows the location of a treasure in
the US. There are three ciphers that determine the following:

    1.The location of the treasure         Key: Unknown
    2.The contents of the treasure(Solved) Key: The Declaration of Independence
    3.The owners of the treasure           Key: Unknown

Use the second cipher to help maintain the accuracy of the decipher program.
"""

import sys

if sys.argv[1].lower() == 'help':
    print("Type the following: python decipher.py <key file> <beale file> <output file>")
    print("For more info, type \"desc\"")
elif sys.argv[1].lower() == 'desc':
    print("")
    print("Title: decipher.py")
    print("Created: Brent Basiano")
    print("Description: This program takes a key to decipher a beale cipher.")
    print("The beale cipher is a coded message that shows the location of a treasure in")
    print("the US. There are three ciphers that determine the following:")
    print("")
    print("    1.The location of the treasure         Key: Unknown")
    print("    2.The contents of the treasure(Solved) Key: The Declaration of Independence")
    print("    3.The owners of the treasure           Key: Unknown")
    print("")
    print("Use the second cipher to help maintain the accuracy of the decipher program.")
else:
    #Read the key text
    with open(sys.argv[1]) as f:
        text = f.read()


    """
    key variable is a hash map for the key text.
    The index is the word position and the value is the word string
    """
    key = {index+1: word for index, word in enumerate(text.split())}


    #Read the text needed to be deciphered
    with open(sys.argv[2]) as f:
        beale = f.read()

    #Split the values and make a list
    beale = list(map(int, beale.split()))

    output = ''.join(key[num][0] for num in beale).lower()

    with open(sys.argv[3], 'w') as f:
        f.write(output)