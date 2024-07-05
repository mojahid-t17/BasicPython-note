import os
# rename the data name of the folders into data-folder from day-1,2,... to date-1,2,...
for i in range(1,11):
    os.rename(f"data-folder/day{i}",f"data-folder/date{i}")