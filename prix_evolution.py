import pandas as pd
import matplotlib.pyplot as plt
from charge_dossier_csv import charger_csv_dossier

# Charger les données
dossier = "Actifs_modifie"
dataframes = charger_csv_dossier(dossier)

for nom_fichier, dataframe in dataframes.items():

    # Convertir la colonne 'Date' au format datetime pour une meilleure manipulation
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], dayfirst=True)

    # Préparer le graphique
    plt.figure(figsize=(14, 8))

    # Tracer les lignes pour les prix d'ouverture, de clôture, les plus hauts et les plus bas
    plt.plot(dataframe['Date'], dataframe['Cloture'], label='Clôture', color='blue')
    plt.plot(dataframe['Date'], dataframe['Ouverture'], label='Ouverture', color='green')
    plt.plot(dataframe['Date'], dataframe['Plus haut'], label='Plus haut', color='red')
    plt.plot(dataframe['Date'], dataframe['Plus bas'], label='Plus bas', color='purple')

    # Ajouter un titre et des étiquettes pour les axes
    plt.title('Évolution du prix de l\'action Dassault au fil du temps')
    plt.xlabel('Date')
    plt.ylabel('Prix de l\'action')
    plt.legend()

    # Améliorer la lisibilité des dates sur l'axe des x
    plt.xticks(rotation=45)

    # Afficher le graphique
    plt.tight_layout()  # Ajuste automatiquement les paramètres de la subplot pour qu'elle s'adapte à la zone d'affichage
    plt.show()
