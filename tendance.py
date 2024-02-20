import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
file_path = 'Actifs_df/Actif_dassault_modifie.csv'  # Remplacez cela par le chemin d'accès réel de votre fichier
data = pd.read_csv(file_path, delimiter=';')

# Convertir 'Date' en datetime
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# Analyse descriptive
descriptive_stats = data[['Ouverture', 'Clôture', 'Plus haut', 'Plus bas']].describe()

# Afficher les statistiques descriptives
print(descriptive_stats)

# Tracer le graphique
plt.figure(figsize=(14, 8))
plt.plot(data['Date'], data['Clôture'], label='Clôture', color='blue')
plt.plot(data['Date'], data['Ouverture'], label='Ouverture', color='green')
plt.plot(data['Date'], data['Plus haut'], label='Plus haut', color='red')
plt.plot(data['Date'], data['Plus bas'], label='Plus bas', color='purple')
plt.title('Évolution du prix de l\'action Dassault au fil du temps')
plt.xlabel('Date')
plt.ylabel('Prix de l\'action')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
