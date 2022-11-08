
# iterating through file is like list or string 

with open("spider.txt") as file:        # automatically close
    for line in file:
        print(line.upper().strip())             # convert text to upper case before printing  strip to remove empty lines(\n)


print ("*********************************************")

print(".......................List...................")
# Readlines get list 

with open("spider.txt") as file:        # automatically close
    lines = file.readlines()   

lines.sort()
print(lines)  # sorted list