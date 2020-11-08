# Homework 10
# Patrick P

# öffne die people.csv Datei im Lesemodus
with open("people.csv", "r") as people_file_out:
    # mit [:1] am Ende skipped man die Headerzeile, also die 0. Zeile bzw. beginnt man mit dem zeilenweise einlesen bei Zeile 1
    Inhalt = people_file_out.readlines()[1:]
    # Inhalt = people_file.read().splitlines()

    # für jede Zeile der zeilenweise eingelesenen Datei in der Var. Inhalt mache...
    for Zeile in Inhalt:
        # ... je Zeile nimm die Elemente die getrennt sind durch ein , und gib sie in Var Zeileninhalt (dürfte ein Arry sein?)
        Zeileninhalt = Zeile.split(",")

        # gib nun die Array Elemente durhc [] angesprochen des Zeileninhalts je Zeile (das macht die for-Schleife) aus
        print(f"{Zeileninhalt[0]} is {Zeileninhalt[1]} years old and {Zeileninhalt[2]}")

    # Frage einen Stringinput ab, um die people.csv zu ergänzen - Dateinamen anzeigen klappt noch nicht
    # Eingabe = str(input(f"Ergänze gerne noch {people_file_out} um eigene Einträge: "))

    # öffne die people.csv im Apend-Modus
    # with open("people.csv", "a+") as people_file_in:
    # Inhalt der Var Eingabe = mein Input schreibe ich ans Ende (Modus append) in das File, danach ist das Script fertig
    # people_file_in.write(Eingabe)

    # Mehrfacheingabe
    # solange wahr = in dem Fall wenn man nicht in die else-clause zum break kommt, passiert...
    while True:
        # ...öffne auf ein neues die people.csv im Apend-Modus
        with open("people.csv", "a") as people_file_in:
            entscheidung = input("Möchtest du weitere Zeilen hinzufügen? y/n")
            if entscheidung == "y":
                Eingabe = str(input(f"Ergänze gerne noch {people_file_out} um eigene Einträge: "))
                # \n damit in eine neue Zeile geschrieben wird
                people_file_in.write("\n" + Eingabe)
            else:
                print("Ok, danke dennoch. Bye")
                break
