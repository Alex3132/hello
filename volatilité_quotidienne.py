import pandas as pd
import matplotlib.pyplot as plt
from charge_dossier_csv import charger_csv_dossier

# Charger les données
dossier = "Actifs_modifie"
dataframes = charger_csv_dossier(dossier)

for nom_fichier, dataframe in dataframes.items():
    dataframe['Différence'] = dataframe['Plus haut'] - dataframe['Plus bas']
    
    # Calculer des statistiques descriptives pour la nouvelle colonne 'Différence'
    stats_volatilite = dataframe['Différence'].describe()
    print("Statistiques de la volatilité basée sur la différence quotidienne/mensuelle entre le plus haut et le plus bas :")
    print(stats_volatilite)
    
    # Visualisation de la volatilité au fil du temps
    plt.figure(figsize=(14, 8))
    plt.plot(dataframe['Date'], dataframe['Différence'], label='Volatilité (Plus haut - Plus bas)', color='orange')
    plt.title('Volatilité de l\'action Dassault au fil du temps')
    plt.xlabel('Date')
    plt.ylabel('Volatilité (Différence entre Plus haut et Plus bas)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
