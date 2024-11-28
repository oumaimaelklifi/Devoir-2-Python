# Exercice 2 : Créer un dictionnaire Stock_FL pour gérer le stock des fruits
# et légumes suivants : Pomme, Banane, Orange, Raisin, Carote, Corgette, Petit Poids, Aubergine …
# Donner une solution pas à pas pour :

# Créer Stock_FL
Stock_FL = {
    'Pomme': 0,
    'Banane': 0,
    'Orange': 0,
    'Raisin': 0,
    'Carote': 0,
    'Petit Poids': 0,
    'Aubergine': 0,
}

# Ajouter les éléments
Stock_FL['Banane'] = 30
Stock_FL['Aubergine'] = 10
Stock_FL['Carote'] = 60
Stock_FL['Orange'] = 10
Stock_FL['Pomme'] = 30
Stock_FL['Raisin'] = 40
Stock_FL['Petit Poids'] = 22


# Afficher Stock_FL par interrogation ou vérification
print(f' le stock des pommes est : {Stock_FL['Pomme']}')

# Afficher Stock_FL par print
print(Stock_FL)

# Afficher tout en parcourant Stock_FL (clé, valeur et clé-valeur)
for key,value in Stock_FL.items():
    print(f'{key} : {value}')

# Donner le nombre de catégorie de produits présents
nombre_categorie=len(Stock_FL)
print(f'Nombre de categorie est : {nombre_categorie}')

# Donner le nombre de produits présents
nombre_produit=0
for key  in Stock_FL.keys():
    nombre_produit+=1
print(f'Nombre de produit present est : {nombre_produit}')

# Copier Stock_FL dans Stock (cas de Copy et cas d’une affectation)
Stock=Stock_FL # Affectation
print(Stock)
Stock=Stock_FL.copy() #copy
print(Stock)

# Que donnera l’instruction Stock_FL.items()
#Il donne a la fois key et value 


# Afficher tout en parcourant Stock_FL (clé, valeur et clé-valeur)
for key,value in Stock_FL.items():
    print(f'{key} : {value}')

# Supprimer un produit (avec del())
del Stock_FL['Aubergine']
print(Stock_FL)

# Vérifier les valeurs de stock et Stock_FL.
for valeur in Stock_FL.values():
    print(valeur)
print()
for valeur in Stock.values():
    print(valeur)

# *Que constatez-vous ? *
#Après avoir supprimé 'Aubergine' de Stock_FL, je remarque que dans Stock_FL,
# l'élément 'Aubergine' a disparu, mais Stock garde l'ancienne version du dictionnaire avec 
# 'Aubergine' (puisque Stock était une copie avant la suppression).


# Utiliser le conditionnel pour afficher un message selon qu’un produit existe
#  ou n’existe pas dans le stock (avec in …)
produit=input('Entrer le produit a rechercher : ')
if produit in Stock_FL :
    print(f"{produit} existe dans le stock ")
else :
    print(f"{produit} n\'existe pas dans le stock.")

# Former une liste des produits présents en stock.
liste_produit=[]
for produit in Stock_FL.values():
    liste_produit.append(produit)
print(liste_produit)

# Former une liste avec les valeurs des quantités du stock
liste_quantite=[]
for key in Stock_FL.keys():
    liste_quantite.append(key)
print(liste_quantite)

# Former la liste et le tuple des produits et leur quantités disponible (avec stock.items()).
liste_produit=[]
liste_tuple=[]

for key,value in Stock_FL.items():
    liste_produit.append((key, value))
    liste_tuple.append((key, value))

liste_tuple=tuple(liste_tuple)
print("Liste des produits et leurs quantités :", liste_produit)
print("Tuple des produits et leurs quantités :", liste_tuple)
    