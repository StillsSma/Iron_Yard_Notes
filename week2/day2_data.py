
with open("data.csv") as open_file:
    contents = open_file.readlines()

# print(contents[2].split(',')[2])

clean_data = []

for line in contents:
    line = line.replace("\n", "")
    clean_data.append(line.split(","))


import csv
with open("data.csv") as open_file:
    contents = csv.DictReader(open_file)

    print(list(contents)[1])
