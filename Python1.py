


import os
import time

print('Hello world')
print(os.getcwd())

os.chdir('C:\\Users\\vdi-student\\Desktop\\nauka\\first_repo')

os.mkdir('new_folder')
os.rename('new_folder', 'new_folder2')
time.sleep(10)
os.rmdir('new_folder2')

