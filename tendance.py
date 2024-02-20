import pandas as pd
import matplotlib.pyplot as plt
import os
import charge_dossier_csv

# Charger les données

dossier = "Actifs_modifie"
fichiers = os.listdir(dossier)

for nom_fichier in fichiers:
    chemin_complet = f"{dossier}/{nom_fichier}"
    data = pd.read_csv(chemin_complet, delimiter=';')

    # Convertir 'Date' en datetime
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

    # Analyse descriptive
    descriptive_stats = data[['Ouverture', 'Cloture', 'Plus haut', 'Plus bas']].describe()

    # Afficher les statistiques descriptives
    print(descriptive_stats)

    nom_entreprise = nom_fichier.split('Actif_')[-1].split('_modifie')[0].capitalize()

    # Tracer le graphique
    plt.figure(figsize=(14, 8))
    plt.plot(data['Date'], data['Cloture'], label='Clôture', color='blue')
    plt.plot(data['Date'], data['Ouverture'], label='Ouverture', color='green')
    plt.plot(data['Date'], data['Plus haut'], label='Plus haut', color='red')
    plt.plot(data['Date'], data['Plus bas'], label='Plus bas', color='purple')
    plt.title(F'Évolution du prix de l\'action {nom_entreprise} au fil du temps')
    plt.xlabel('Date')
    plt.ylabel('Prix de l\'action')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
