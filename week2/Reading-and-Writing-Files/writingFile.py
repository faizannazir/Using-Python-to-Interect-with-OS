# file modes
#  r  for read only  (default)
#  w  for write only   create file if doesnot exist if exist overwrite its content
#  a  for append        add content at the end of existing file
#  r+ for read-write 
#  b  for binary mode 
#  x  for exclusive creation , failing if the file already exist
#  t  for text mode (default)

with open("novel.txt",'w') as file:
    file.write("It was a dark and a stormy night")
