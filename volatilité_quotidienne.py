import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Actifs_df/Actif_dassault_modifie.csv'  # Remplacez cela par le chemin d'accès réel de votre fichier
data = pd.read_csv(file_path, delimiter=';')
# Charger les données
data['Différence'] = data['Plus haut'] - data['Plus bas']

# Calculer des statistiques descriptives pour la nouvelle colonne 'Différence'
stats_volatilité = data['Différence'].describe()
print("Statistiques de la volatilité basée sur la différence quotidienne/mensuelle entre le plus haut et le plus bas :")
print(stats_volatilité)

# Visualisation de la volatilité au fil du temps
plt.figure(figsize=(14, 8))
plt.plot(data['Date'], data['Différence'], label='Volatilité (Plus haut - Plus bas)', color='orange')
plt.title('Volatilité de l\'action Dassault au fil du temps')
plt.xlabel('Date')
plt.ylabel('Volatilité (Différence entre Plus haut et Plus bas)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
