import csv
infile = open("data.csv")
data = csv.reader(infile)
names = next(data) # column names
for row in data:
    print(row[1]) # 2nd column