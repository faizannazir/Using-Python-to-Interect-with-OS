import os

# remove file if exist 
if(os.path.exists("novel.txt")):
    os.remove("novel.txt")
    print("Sucessfully removed ")
else:
    print("file not exist ")
