import json
import os
from dotenv import load_dotenv
import argparse

# Charger les variables d'environnement
load_dotenv()

# Charger la configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Analyser les arguments en ligne de commande
parser = argparse.ArgumentParser(description='SenseUltra_Trading_V2')
parser.add_argument('--coin', type=str, default='btc', help='Cryptomonnaie à trader')
parser.add_argument('--profile', type=str, default='debutant', help='Profil utilisateur')
parser.add_argument('--mode', type=str, default='normal', help='Mode de fonctionnement')
args = parser.parse_args()

# Exemple : Afficher la configuration
print(f"Trading {args.coin} avec le profil {args.profile} en mode {args.mode}")

# TODO : Implémenter la logique de trading basée sur la configuration et les arguments