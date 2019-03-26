'''
This program encodes a message using the Vignere Cipher and decrypts it afterwards.
CS 111, Fall 2018
Date: October 2nd, 2018
Names: Zack Johnson and Jordan Navarro
'''

def main():
    # Header.
    print("* * * VIGNERE CIPHER * * *")

    # Ask the user for a message to encode and a password.
    msg = input("Enter a message to encrypt: ")
    password = input("Enter a password to encrypt this message: ")

    # Convert message and password to lowercase and remove spaces.
    msg = msg.lower()
    msg = msg.replace(" ", "")
    password = password.lower()
    password = password.replace(" ", "")

    # Store the alphabet.
    codeAlphabet = "abcdefghijklmnopqrstuvwxyz"

    # Implement the encrypt algorithm as described in the PDF.
    cipherText = ""
    for i in range(len(msg)):
        # Find the position in the alphabet of the ith letter of the message.
        m = msg[i] 
        msgIndex = codeAlphabet.find(m)
        # Find the position in the alphabet of the ith letter of the password.
        # If the password is shorter than the message, then the % (modulo) loops back to the beginning of the password.
        p = password[i % len(password)]
        keyLetterIndex = codeAlphabet.find(p)
        # Find the new letter in the alphabet and append it to the code.
        cipherLetter = codeAlphabet[(msgIndex + keyLetterIndex) % 26]
        cipherText = cipherText + cipherLetter

    # Print out the encrypted message.
    print("\nYour encrypted message is:", cipherText)

    # Implement the decrypt algorithm as described in the PDF.
    test = ""
    for i in range(len(cipherText)):
        # Find the position in the alphabet of the ith letter of the message.
        c = cipherText[i] 
        cipherIndex = codeAlphabet.find(c)
        # Find the position in the alphabet of the ith letter of the password.
        p = password[i % len(password)]
        keyLetterIndex = codeAlphabet.find(p)
        # Find the new letter in alphabet and subtract it from the code.
        testLetter = codeAlphabet[(cipherIndex - keyLetterIndex) % 26]
        test = test + testLetter
    
    # Print out the decrypted message.
    print("\nCheck -- your decrypted message is:", test)

    # Footer.
    print("* * * END VIGNERE CIPHER * * *")

main()
