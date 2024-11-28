
# Exercice 1 : Créer un programme pour gérer les notes des étudiants calculer leur moyenne
#  et déterminer s'ils sont admis ou non, en se basant sur les fonctions et les listes.


def moyenne(notes):
    return 0 if len(notes) == 0 else sum(notes) / len(notes)

def est_admis(notes):
    moyenne_notes = moyenne(notes)
    return "Admis" if moyenne_notes >= 10 else "N'est pas admis"

def gerer_notes_etudiant():
    etudiants = [] 
    n = int(input('Combien d\'étudiants souhaitez vous ajouter ? '))

    for i in range(n):
        nom = input('Nom de l\'étudiant : ')
        prenom = input('Prénom de l\'étudiant : ')
        nbr_note = int(input("Entrez le nombre de notes pour cet étudiant : "))
        
        notes = []
        for j in range(nbr_note):
            note = float(input(f"Entrez la note {j+1} de l'étudiant {prenom} {nom} : "))
            notes.append(note)
        
        moyenne_etudiant = moyenne(notes)
        resulat_etudiant = est_admis(notes)

        etudiants.append(
            { 
              'Nom': nom,
              'Prenom': prenom,
              'note': notes,
              'moyenne': moyenne_etudiant,
              'Resultat': resulat_etudiant
            }
        )

    print('=== Résultats ===')
    for etudiant in etudiants:
    
        print(f"Nom : {etudiant['Nom']} {etudiant['Prenom']}")
        print(f"Notes : {', '.join(map(str, etudiant['note']))}")
        print(f"Moyenne : {etudiant['moyenne']:.2f}")
        print(f"Résultat : {etudiant['Resultat']}")
      
gerer_notes_etudiant()
