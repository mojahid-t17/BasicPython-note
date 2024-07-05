import os
# # make a directory named "data-folder"
# os.mkdir('data-folder')

# if data-folder doesn't exist then create the data folder
if (not os.path.exists('data-folder')):
    os.mkdir('data-folder')

# create 10 folder into data-folder
for i in range(1,11):
    os.mkdir(f"data-folder/day{i}")