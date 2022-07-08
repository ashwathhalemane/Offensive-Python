import os
import zipfile

cwd = os.listdir() # here we know there is a file called secret_zip 

secret_zip = "" # name of the secret.zip file will be populated after the loop

secret = 'secret.zip' # this is known

for match in cwd:
    if secret in match:
        secret_zip+=secret # append secret_zip from cwd

with zipfile.ZipFile(secret_zip, 'r') as myzip: # read zip file
    myzip.printdir() # printing the content of zip file


