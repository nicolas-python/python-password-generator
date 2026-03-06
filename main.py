#python-password-generator
# menü
def password_generator():
    choice = None

    while choice not in ["1","2","3","4"]:
        print("1 : Passwort Generiren")
        print("2 : Wählen sie länge des Passwortes")
        print("3 : Wollen sie ein Sonderzeichen?")
        print("4 : Beenden")

        choice = input("Wähle eine Option:")
        print("Du häst gewählt:", choice)

        if choice not in ["1","2","3","4"]:
            print("Ungültige Option, bitte erneut zwischen 1,2,3,4  wählen.")

    return choice

def password_laeng():
        print("Wie lang soll ihr password sein")
        laeng = int(input("Länge:"))
        return laeng

def password_generator_code():
    password_list = []
    password_list.append("A")
    password_list.append("B")
    password_list.append("C")
    password = "".join(password_list)
    print(password)

#start werte ändern sich

leang = 8


while True:
    choice = password_generator()

    match choice :

        case "1" :
            print("Passwort Generiren")
            password_generator_code()

        case "2" :
            print("Wählen sie länge des Passwortes")
            leang = password_laeng()
            print("Dein Passwort soll ", leang,"Zeichen sein"
                  )
        case "3":
            print("Wollen sie ein Sonderzeichen?")
            sonderzeichen = input("Wollen sie das Passwort mit sonderzeichen? (y/n):")

        case "4":
            print("Beenden")
            break


