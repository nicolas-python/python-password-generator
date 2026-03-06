#python-password-generator
#menü
def passwort_generator():
    choice = None

    while choice not in ["1","2","3","4"]:
        print("1 : Passwort Generator")
        print("2 : Wählen sie länge des Passwortes")
        print("3 : Wollen sie ein Sonderzeichen?")
        print("4 : Beenden")

        choice = input("Wähle eine Option")
        print("Du häst gewählt:", choice)

        if choice not in ["1","2","3","4"]:
            print("Ungültige Option, bitte erneut zwischen 1,2,3  wählen.")

    return choice

