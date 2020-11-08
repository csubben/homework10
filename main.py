# Homework 10
# Patrick P
# öffne die people.csv Datei im Lesemodus

with open("people.csv", "r") as people_file_out:
    # mit [:1] am Ende skipped man die Headerzeile, also die 0. Zeile bzw. beginnt man mit dem zeilenweise einlesen bei Zeile 1
    Inhalt = people_file_out.readlines()[1:]
    #Inhalt = people_file.read().splitlines()
    for Zeile in Inhalt:
        Zeileninhalt = Zeile.split(",")
        print(f"{Zeileninhalt[0]} is {Zeileninhalt[1]} years old and {Zeileninhalt[2]}")


Eingabe = str(input(f"Ergänze gerne noch {people_file_out} um eigene Einträge: "))
#with open("people.csv", "w") as people_file_in:
    #Ergaenzung = people_file_in.append({Eingabe}) --- funktioniert so nicht
    
