
# Exercice 3 : Créer une base de données fonctionnant à l’aide d’un dictionnaire, 
# dans lequel on enregistre les noms des étudiants, leur moyenne et leur classement.
# On suppose que le dictionnaire ne contient pas plusieurs valeurs identiques.
# Le programme doit proposer un menu qui demande à l'utilisateur de choisir une opération parmi :
# R : Remplir la base de données
# C : Consulter les notes d'un étudiant
# T: Terminer le programme
# La saisie des données, doit se faire tant que l'utilisateur le souhaite.


etudiants_db = {}

def remplir_base():
    while True:
        nom = input("Entrez le nom de l'étudiant : ")
        moyenne = float(input("Entrez la moyenne de l'étudiant : "))
        classement = input("Entrez le classement de l'étudiant : ")


        etudiants_db[nom] = {"moyenne": moyenne, "classement": classement}
        
    
        continuer = input("Souhaitez-vous ajouter un autre étudiant ? (O/N) : ").upper()
        if continuer != 'O':
            break

def consulter_notes():
    nom = input("Entrez le nom de l'étudiant à consulter : ")
    if nom in etudiants_db:
        etudiant = etudiants_db[nom]
        print(f"Nom : {nom}")
        print(f"Moyenne : {etudiant['moyenne']}")
        print(f"Classement : {etudiant['classement']}")
    else:
        print(f"Aucun étudiant trouvé avec le nom {nom}.")

def menu():
    while True:
        print("\nMenu :")
        print("R : Remplir la base de données")
        print("C : Consulter les notes d'un étudiant")
        print("T : Terminer le programme")
        
        choix = input("Choisissez une option (R/C/T) : ").upper()
        
        if choix == 'R':
            remplir_base()
        elif choix == 'C':
            consulter_notes()
        elif choix == 'T':
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
            
menu()
