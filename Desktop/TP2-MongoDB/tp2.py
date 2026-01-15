import os
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

# 1. Connexion sécurisée
load_dotenv()
uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

# On sélectionne la base de données (elle se créera toute seule)
db = client['tp_nosql'] 
# On sélectionne la collection (équivalent de la table)
users_col = db['utilisateurs']

def run_tp():
    print("Nettoyage de la collection (pour éviter les doublons)...")
    users_col.delete_many({}) # On vide avant de remplir

    # --- ÉTAPE 1 : INSERTION DES DONNÉES (Consigne TP) ---
    print("Insertion des utilisateurs...")
    
    donnees = [
        {
            "nom": "Dupont", "prenom": "Jean", "age": 30,
            "email": "jean.dupont@example.com",
            "roles": ["admin", "utilisateur"],
            "adresse": {"rue": "123 Rue de la Paix", "ville": "Paris", "codePostal": "75001"},
            "dateCreation": datetime.now()
        },
        {
            "nom": "Martin", "prenom": "Sophie", "age": 25,
            "email": "sophie.martin@example.com",
            "roles": ["utilisateur"],
            "adresse": {"rue": "45 Avenue des Champs", "ville": "Lyon", "codePostal": "69002"},
            "dateCreation": datetime.now()
        },
        {
            "nom": "Bernard", "prenom": "Pierre", "age": 40,
            "email": "pierre.bernard@example.com",
            "roles": ["utilisateur"],
            "adresse": {"rue": "78 Boulevard de la Liberté", "ville": "Marseille", "codePostal": "13005"},
            "dateCreation": datetime.now()
        }
    ]
    
    users_col.insert_many(donnees)
    print("3 utilisateurs insérés avec succès !")
    print("-" * 50)

    # --- ÉTAPE 2 : LES REQUÊTES (Consigne TP) ---

    # Requête A : Afficher tous les utilisateurs
    print("1. Tous les utilisateurs :")
    tous = users_col.find()
    for u in tous:
        print(f"- {u['prenom']} {u['nom']}")

    print("-" * 20)

    # Requête B : Âge >= 30 ans ($gte = greater than or equal)
    print("2. Utilisateurs de 30 ans ou plus :")
    vieux = users_col.find({"age": {"$gte": 30}})
    for u in vieux:
        print(f"- {u['prenom']} ({u['age']} ans)")

    print("-" * 20)

    # Requête C : Rôle Admin
    print("3. Les Admins :")
    admins = users_col.find({"roles": "admin"})
    for u in admins:
        print(f"- {u['prenom']} {u['nom']}")

if __name__ == "__main__":
    run_tp()