import matplotlib.pyplot as plt
from charge_dossier_csv import *

# Charger les données
dossier = "Actifs_modifie"
dataframes = charger_csv_dossier(dossier)

for nom_fichier, dataframe in dataframes.items():

    # Convertir 'Date' en datetime
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], dayfirst=True)

    # Analyse descriptive
    descriptive_stats = dataframe[['Ouverture', 'Cloture', 'Plus haut', 'Plus bas']].describe()

    # Afficher les statistiques descriptives
    print(descriptive_stats)

    nom_entreprise = nom_fichier.split('Actif_')[-1].split('_modifie')[0].capitalize()

    # Tracer le graphique
    plt.figure(figsize=(14, 8))
    plt.plot(dataframe['Date'], dataframe['Cloture'], label='Clôture', color='blue')
    plt.plot(dataframe['Date'], dataframe['Ouverture'], label='Ouverture', color='green')
    plt.plot(dataframe['Date'], dataframe['Plus haut'], label='Plus haut', color='red')
    plt.plot(dataframe['Date'], dataframe['Plus bas'], label='Plus bas', color='purple')
    plt.title(f"Évolution du prix de l'action {nom_entreprise} au fil du temps")
    plt.xlabel('Date')
    plt.ylabel("Prix de l'action")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
