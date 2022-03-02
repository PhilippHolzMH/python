from birthday import berechnung_alter
from folder import create_fold
success = False

while success == False:
    nachname = input("So gebe er mir den Nachnamen: ")
    tag,monat,jahr = map(int, input("Wann hat er das Licht der Welt entdeckt? ").split('.'))
    alter = berechnung_alter (jahr, monat, tag)

    if alter > 17:

        success = create_fold (nachname + str(alter), str(alter))
    else:
        print ("Sorry du bist zu jung")