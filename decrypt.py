#!/usr/bin/env python3



import os
from cryptography.fernet import Fernet


files= [] #this is the list that will be used to store the files in current directory.


for file in os.listdir():
    if file == "encrypt.py" or file == "keyfile.key" or file == "decrypt.py": ## you must skip these 3 files otherwise you may not be able to decrypt the file or encrypt again.
        continue
    if os.path.isfile(file):
        files.append(file)

with open("keyfile.key", "rb") as key: # retrieve the key from the stored file
    theKey = key.read()


word = "Apple"
i = 0
flag = 0

while(i<3):
    guess_word = input("Try to guess the password:")
    if guess_word == word:
        print("Decryption is starting...")
        for file in files:
            with open(file, "rb") as each_file:  #read each file in binary mode and retrieve their encrypted content
                file_content = each_file.read()
            
            decrypted_contents = Fernet(theKey).decrypt(file_content) #decrypt the retrieved content

            with open(file, "wb") as weach_file:
                weach_file.write(decrypted_contents) #write the decrypted content on the same file
        print("Your files are Decrypted successfully!!")
        flag = 1
        break
    else:
        print("Please try again...")
        i+=1
    


    if i==3 and flag == 0:
        print("Your files will remain DECRYPTED HAHAHA")

