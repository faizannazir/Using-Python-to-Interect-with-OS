file = open("spider.txt")
print(file.readline())  # read 1 line from current position.  object updates current position in file
print(file.readlines())  # read multiples lines from current position return list
print(file.read())      # read remaining text in files 
file.close()            # close the file 


