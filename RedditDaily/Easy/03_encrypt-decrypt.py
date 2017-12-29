#encyrpter and decrypter

import codecs
selection = int(input("Would you like to encrypt of decrypt? \n \n 1.)Encrypt \n 2.)Decrypt \n"))
if selection == 1 or selection == "E" or selection == "e" or selection == "encrypt" or selection == "Encrypt" :
    startPhrase = input("Enter the phrase to be encrypted: \n")
    final = codecs.encode(startPhrase, "rot13")
if selection == 2 or selection == "D" or selection == "d" or selection == "decrypt" or selection == "Decrypt" :
    startPhrase = input("Enter the phrase to be decrypted: \n")
    final = codecs.decode(startPhrase, "rot13")
print(final)
