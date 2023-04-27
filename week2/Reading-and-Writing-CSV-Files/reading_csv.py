import os, csv

dir = os.path.abspath(".")
files = os.path.join(dir,"file.csv")
print(files)
f= open(file=files)
csv_reader = csv.reader(f)

f.close()