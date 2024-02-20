import pandas as pd
import matplotlib.pyplot as plt

from charge_dossier_csv import charger_csv_dossier

dossier = "Actifs_modifie"
dataframes = charger_csv_dossier(dossier)


for nom_fichier in dataframes:
    chemin_complet = f"{dossier}/{nom_fichier}"
    data = pd.read_csv(chemin_complet, delimiter=';')

    # Convertir la colonne 'Date' au format datetime pour une meilleure manipulation
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

    # Préparer le graphique
    plt.figure(figsize=(14, 8))

    # Tracer les lignes pour les prix d'ouverture, de clôture, les plus hauts et les plus bas
    plt.plot(data['Date'], data['Cloture'], label='Clôture', color='blue')
    plt.plot(data['Date'], data['Ouverture'], label='Ouverture', color='green')
    plt.plot(data['Date'], data['Plus haut'], label='Plus haut', color='red')
    plt.plot(data['Date'], data['Plus bas'], label='Plus bas', color='purple')

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
