import os , datetime


# get file size in bytes 
size = os.path.getsize("file.py")
print(" File size: ",size,"Bytes")

# check last modified time
# unix time stamp
timestamp = os.path.getmtime("file.py")
print(" Time stamp: ",timestamp)

last_modified =datetime.datetime.fromtimestamp(timestamp)
print(" Date Time: ",last_modified)

# abs path take file name and turn it to absolute path
abs_path = os.path.abspath("file.py")
print(" Absolute Path: ",abs_path)