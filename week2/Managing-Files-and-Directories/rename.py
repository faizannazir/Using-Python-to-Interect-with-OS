import os 

current_name ='file.txt'
new_name = 'file.py'
# rename file if exist 
if os.path.exists(current_name):
    os.rename(current_name,new_name)
    print(f"{current_name} successfully changed to {new_name}")
else:
    print(f"{current_name} not exist")