import pandas as pd
import os


def charger_csv_dossier(dossier):
    fichiers_dataframes = {}  # Dictionnaire pour stocker les noms de fichiers et les DataFrames
    fichiers = os.listdir(dossier)  # Lister tous les fichiers dans le dossier

    for nom_fichier in fichiers:
        # Construire le chemin complet vers le fichier
        chemin_complet = os.path.join(dossier, nom_fichier)
        # Vérifier si c'est un fichier CSV
        if os.path.isfile(chemin_complet) and nom_fichier.endswith('.csv'):
            # Charger le fichier CSV dans un DataFrame
            data = pd.read_csv(chemin_complet, delimiter=';')
            # Ajouter le DataFrame au dictionnaire avec le nom du fichier comme clé
            fichiers_dataframes[nom_fichier] = data

    return fichiers_dataframes
