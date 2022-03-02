from datetime import date
today = date.today()

def berechnung_alter(geburtsjahr, geburtsmonat, geburtstag):
    
    diff = today.year - geburtsjahr
    hattegeb = (today.month, today.day) < (geburtsmonat, geburtstag)
    if hattegeb : 
        return diff -1
    return diff

