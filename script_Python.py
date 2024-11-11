import requests
import pandas as pd

# Paramètres de l'API
APP_ID = 'XXX'
APP_KEY = 'XXX'
BASE_URL = 'https://api.edamam.com/api/food-database/v2/parser'

# Paramètres de recherche
query = "champagne"  # Rechercher "champagne" dans les produits
params = {
    'app_id': APP_ID,
    'app_key': APP_KEY,
    'ingr': query
}

# Envoi de la requête
response = requests.get(BASE_URL, params=params)
print("Statut de la réponse :", response.status_code)
print("Contenu de la réponse :", response.json())  # Affiche la réponse JSON
data = response.json()

# Extraction des informations nécessaires
items = []
for i, food in enumerate(data.get('hints', [])):
    if i >= 10:  # Limiter à 10 produits
        break
    food_data = food['food']
    item = {
        'foodId': food_data.get('foodId'),
        'label': food_data.get('label'),
        'category': food_data.get('category'),
        'foodContentsLabel': food_data.get('foodContentsLabel', ''),
        'image': food_data.get('image', '')
    }
    items.append(item)

# Sauvegarde dans un fichier CSV
if items:  # Vérifie que 'items' contient des données
    df = pd.DataFrame(items)
    df.to_csv("produits_champagne.csv", index=False)
    print("Données sauvegardées dans 'produits_champagne.csv'")
else:
    print("Aucune donnée récupérée. Vérifie les paramètres de la requête API.")
