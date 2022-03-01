import csv
from csv import reader
with open ('studentendb.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['vorname'], row['nachname'])

print(row)