# Ce fichier coordonne les grandes étapes du distributeur :
# 1. vérifier le code PIN ;
# 2. afficher le menu ;
# 3. appeler les fonctions de tools quand le client choisit une action.

from data import nom_utilisateur, pin_compte, plafond, solde_actuel
from tools import authentifier, date_et_heure, enregistrer_transaction, verif_retrait


def afficher_historique(historique):
    """Affiche les retraits effectués pendant cette session."""
    if len(historique) == 0:
        print("Aucune transaction.")
    else:
        for transaction in historique:
            print(transaction)

def effectuer_retrait(solde_actuel, historique):
    """Demande un montant, le vérifie, puis met à jour le solde et l'historique."""
    montant_str = input("Montant à retirer : ")

    # tools vérifie que le montant est correct et renvoie un message d'erreur
    # ou le montant sous forme de nombre entier.
    retrait_valide, resultat = verif_retrait(montant_str, solde_actuel, plafond)
    if not retrait_valide:
        print(resultat)
        return solde_actuel

    montant = resultat
    nouveau_solde = solde_actuel - montant

    # On garde une trace du retrait dans l'historique de la session.
    date, heure = date_et_heure()
    transaction = enregistrer_transaction(
        nom_utilisateur, "debit", montant, date, heure
    )
    historique.append(transaction)

    print(f"Retrait effectué. Nouveau solde : {nouveau_solde} €.")
    return nouveau_solde


def menu_principal(solde_actuel):
    """Affiche les choix et lance l'action choisie par le client."""
    historique = []

    while True:
        print("\n==== MENU ====")
        print("1. Consulter votre solde")
        print("2. Retirer de l'argent")
        print("3. Consulter l'historique")
        print("4. Quitter")
        choix = input(f"Que souhaitez-vous faire {nom_utilisateur} ? ")

        if choix == "1":
            print(f"Votre solde est de {solde_actuel} €.")
        elif choix == "2":
            solde_actuel = effectuer_retrait(solde_actuel, historique)
        elif choix == "3":
            afficher_historique(historique)
        elif choix == "4":
            print("Merci d'avoir utilisé notre service. Au revoir !")
            return
        else:
            print("Choix invalide. Veuillez réessayer.")


def main():
    """Lance le programme et n'ouvre le menu qu'après authentification."""
    print("=" * 40)
    print("       BIENVENUE À LA BANQUE")
    print("=" * 40)
    print("Vous disposez de 3 tentatives.")

    # authentifier renvoie True si le PIN est correct, False sinon.
    if authentifier(pin_compte):
        print("Bienvenue dans votre espace bancaire !")
        print("Votre solde actuel est de", solde_actuel, "euros.")
        menu_principal(solde_actuel)
    else:
        print("La session est terminée. À bientôt !")


# Cette condition lance main seulement quand on exécute ce fichier directement.
if __name__ == "__main__":
    main()
