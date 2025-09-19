import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypter.py" or file == "keyfile.key" or file == "decrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("keyfile.key", "rb") as key_file:
    key = key_file.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    decrypted = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(decrypted)
# Clear the contents of "keyfile.key"
with open("keyfile.key", "w") as file:
    file.write("")
