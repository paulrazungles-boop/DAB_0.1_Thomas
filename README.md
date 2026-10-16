# 2026_2027_nsi_prem__projet1__dab__RAZUNGLES
DAB (distributeur automatique de billet)
RAZUNGLES Paul
DUPONT DE DINECHIN Arthur
FORTES Camille
L'HERMITE Hippolyte

# Projet DAB - NSI Première

## Répartition des rôles et des tâches (Groupe de 4)

- **Paul RAZUNGLES — Logique de Retrait, Caisse Limitée & Algorithme de Billets**
  - Vérification des conditions de retrait (multiple de 10, solde suffisant, respect du plafond).
  - Gestion de la caisse limitée : définition d'un stock initial de billets dans le DAB (ex: 10 billets de 50 €, 20 de 20 €, 50 de 10 €).
  - Calcul d'optimisation : algorithme de distribution avec le moins de billets possible en s'adaptant en temps réel au stock restant dans la machine.

- **Camille FORTES — Interface, Menus & Ticket de caisse**
  - Menu principal interactif et gestion fluide de la navigation.
  - Mise en place des choix rapides (ex: 20 €, 50 €, 100 €) et de la saisie d'un montant libre.
  - Module Ticket de caisse : proposition d'imprimer un reçu textuel à la fin d'un retrait réussi (affichage de la date, du montant, des billets distribués et du solde restant).

- **Arthur DUPONT DE DENECHIN — Gestion des Comptes, Authentification & Sécurité**
  - Création et choix du compte au démarrage (dictionnaire des utilisateurs avec code PIN, solde et plafond).
  - Gestion de la sécurité : blocage de la carte/du compte après 3 essais de code PIN infructueux.

- **Hippolyte L'HERMITE — Mini-Relevé, Tests Unitaires & Documentation**
  - Historique des transactions : stockage des opérations de la session sous forme de liste et ajout d'une option de consultation dans le menu.
  - Écriture de la fonction `lancer_les_tests()` regroupant tous les `assert` pour valider les calculs et les cas limites.
  - Rédaction des docstrings et mise en forme complète du fichier `README.md`.

## Fonctionnalités du projet
- Création et gestion des comptes avec vérification du code PIN.
- Saisie personnalisée d'un montant libre combinée à des choix rapides.
- Module de ticket de caisse interactif en fin de transaction.
- Mini-relevé des opérations de la session.
- Caisse de billets limitée avec gestion intelligente des stocks.