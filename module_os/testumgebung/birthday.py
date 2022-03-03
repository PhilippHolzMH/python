def berechnung_alter(birthdate, today):
    
    diff = today.year - birthdate.year
    hattegeb = (today.month, today.day) < (birthdate.month, birthdate.day)
    if hattegeb : 
        return diff -1
    return diff

