def validate_input(message):
    return(message)

def enrgistrer_transaction(nom,type_operation,montant,date,heure ):
    return(nom,type_operation,montant,date,heure)

def is_a_number(nb_str):
    return (nb_str)

def code_pin(pin):
    return(pin)

def plafond(debit_max):
    return(debit_max)

def solde(credit):
    return(credit)

def lancer_les_tests(tests):
    return(tests)

def quitter(faux):
    return(faux)


from datetime import datetime

# Fonctions réparties selon les rôles décrits dans le README :
# Arthur DUPONT DE DINECHIN : authentification et sécurité du code PIN.
# Paul RAZUNGLES : vérification des conditions de retrait.
# Hippolyte L'HERMITE : création des lignes d'historique des transactions.


def authentifier(pin_correct):
    """Vérifie le code PIN avec trois tentatives maximum."""
    tentatives = 0

    while tentatives < 3:
        pin = input("Votre code PIN : ")
        if pin == pin_correct:
            print("Code PIN correct !")
            return True

        tentatives += 1
        restantes = 3 - tentatives
        print("Oups ! Le code PIN saisi est incorrect.")
        if restantes > 0:
            print("Il vous reste", restantes, "tentative(s).")

    print("Accès refusé. Votre carte est bloquée pour cette session.")
    return False


def verif_retrait(montant_str, solde_compte, plafond):
    if not montant_str.isdigit():
        return False, "Veuillez entrer un nombre entier valide."

    montant = int(montant_str)
    if montant <= 0:
        return False, "Veuillez saisir un montant positif."
    if montant > plafond:
        return False, f"Le montant dépasse le plafond de {plafond} €."
    if montant % 10 != 0:
        return False, "Le montant doit être un multiple de 10."
    if montant > solde_compte:
        return False, "Solde insuffisant."
    return True, montant


def enregistrer_transaction(nom, type_operation, montant, date, heure):
    if type_operation == "credit":
        return f"{nom} a crédité {montant} le {date} à {heure}"
    return f"{nom} a débité {montant} le {date} à {heure}"


def date_et_heure():
    maintenant = datetime.now()
    return maintenant.strftime("%d/%m/%Y"), maintenant.strftime("%H:%M:%S")