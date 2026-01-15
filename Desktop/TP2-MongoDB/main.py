import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# 1. Charger les variables
load_dotenv()
uri = os.getenv("MONGO_URI")

# Vérification que l'URI est bien chargée
if not uri:
    print("Erreur : La variable MONGO_URI est vide. Vérifie ton fichier .env")
    exit()

# 2. Création du client MongoDB
# server_api uses the Stable API (recommandé pour Atlas)
client = MongoClient(uri, server_api=ServerApi('1'))

def test_connection():
    try:
        # 3. Envoi d'un "Ping" pour vérifier que ça marche
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
        # (Bonus) Lister les bases de données existantes
        dbs = client.list_database_names()
        print(f"Bases de données trouvées : {dbs}")

    except Exception as e:
        print(f"Erreur de connexion : {e}")

if __name__ == "__main__":
    test_connection()