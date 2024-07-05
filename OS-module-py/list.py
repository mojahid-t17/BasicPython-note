import os
# see the list of folder in "data-folder"
folders=os.listdir('data-folder')
print(folders)
# for folder in folders:
#     # print(folder)
#     # print(os.listdir(f"data-folder/{folder}"))

# getting the current working directory: 
print(os.getcwd())

# delete a directory like date10
if(os.path.exists('data-folder/date10')):
    os.rmdir('data-folder/date10')
else:
    print('there is no directory named date10')