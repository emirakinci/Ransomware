# Ransomware

This program aims to encrypt and decrypt files located within a repository. 
For the encryption algorithm, Fernet is used because of the simplicity of its implementation and its strong 128-bit symmetric encryption capability.

How does the code work?
  encrypt.py :
    -> Creates a key by using Fernet 
    -> Iterates over the files in the same directory as the program is stored and ensures they're not a directory.
    -> Stores all file names in a list.
    -> Afterwards, writes the key into a file to use it for the decryption later.
    -> Moreover, for each file stored in the list, the program reads its content and encrypts it.
    -> Lastly, writes the encrypted content on the file.

  decrypt.py :
    -> Retrieves the key from the file that stores the key.
    -> Iterates over the files and decryptes each of them by using the key.
    -> Asks the user for a specific word by giving him 3 attempts to insert the correct one.
    -> If the word is true, all the files are decrypted.
    -> If not they remain encrypted.
    
