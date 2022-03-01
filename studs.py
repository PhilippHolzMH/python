import csv
from datetime import date
from ntpath import join
today = date.today()
def berechnung_alter(geburtsjahr, geburtsmonat, geburtstag):
    
    diff = today.year - geburtsjahr
    hattegeb = (today.month, today.day) < (geburtsmonat, geburtstag)
    if hattegeb : 
        return diff -1
    return diff

vorname,nachname = map(str,input("please type your name: ").split ())
tag,monat,jahr = map(int, input("Enter a date: ").split('.'))
alter = berechnung_alter (jahr, monat, tag)

if alter > 18:
    with open ('studentendb.csv', 'a', newline='') as input_file:
        writer = csv.writer(input_file)
        writer.writerow([vorname,nachname,alter])
else:
    print ("Sorry du bist zu jung")

