#python-password-generator
# menü
def password_generator():
    choice = None

    while choice not in ["1","2","3","4"]:
        print("1 : Passwort Generieren")
        print("2 : Wählen sie länge des Passwortes")
        print("3 : Wollen sie ein Sonderzeichen?")
        print("4 : Beenden")

        choice = input("Wähle eine Option:")
        print("Du hast gewählt:", choice)

        if choice not in ["1","2","3","4"]:
            print("Ungültige Option, bitte erneut zwischen 1,2,3,4  wählen.")

    return choice

def password_laenge():
        print("Wie lang soll ihr password sein")
        laenge = int(input("Länge:"))
        return laenge


def password_generator_code(leange):

    buchstaben_liste = ["A","B","C","D","E","F","G","H","I","J","K","L",
                        "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                        "a","b","c","d","e","f","g","h","i","j","k","l","m",
                        "n","o","p","q","r","s","t","u","v","w","x","y","z"]

    if sonderzeichen == "y":
        alle_zeichen = buchstaben_liste + password_sonderzeichen()

    else :
        alle_zeichen = buchstaben_liste
    password_list = []

    for i in range(leange):
        password_list.append(alle_zeichen[i % len(alle_zeichen)])

    password = "".join(password_list)
    print("Dein Passwort:",password)


def password_sonderzeichen():
    sonderzeichen_list = ["!", "?", "#", "$", "&"]
    return sonderzeichen_list


#start
leange = 8
sonderzeichen = ""

while True:
    choice = password_generator()

    match choice :

        case "1" :
            print("Passwort Generieren")
            password_generator_code(leange)


        case "2" :
            print("Wählen sie länge des Passwortes")
            leange = password_laenge()
            print("Dein Passwort soll ", leange,"Zeichen sein")


        case "3":
            print("Wollen sie ein Sonderzeichen?")
            sonderzeichen = input("Wollen sie das Passwort mit sonderzeichen? (y/n):")


        case "4":
            print("Beenden")
            break



