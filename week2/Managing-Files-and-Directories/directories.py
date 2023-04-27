import os

# Print currently working directory
pwd = os.getcwd()
print(" Working directory: ",pwd)

# make directory
os.mkdir("new_dir")

print(" I am currently in ",pwd)

# Change currently working directory 
os.chdir("new_dir")
pwd = os.getcwd()
print(" I am now in ",pwd)


#  Remove directory
os.chdir("..")              # change directories
os.rmdir("new_dir")         # only can remove empty directory

# List of sub directory
list = os.listdir()    # can pass directory 
print(list)

# check results of listdir() files or directory 

for name in list:
    if os.path.isfile(name):
        print(f"{name} is file")
    else:                               # os.isdir(name) also available
        print(f"{name} is directory")

# use  os.path.join() function to join path so script can work on any OS