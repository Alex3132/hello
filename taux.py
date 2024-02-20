import pandas as pd

# Étape 1: Charger les données
file_path = 'Actifs_df/Actif_dassault_modifie.csv'  # Assurez-vous que le chemin est correct
data_dassault_modifie = pd.read_csv(file_path, delimiter=';')

# Convertir la colonne 'Date' en datetime pour faciliter le regroupement
data_dassault_modifie['Date'] = pd.to_datetime(data_dassault_modifie['Date'], dayfirst=True)

# Définir l'année et le trimestre pour chaque ligne
data_dassault_modifie['Année'] = data_dassault_modifie['Date'].dt.year
data_dassault_modifie['Trimestre'] = data_dassault_modifie['Date'].dt.to_period('Q')

# Calculer les rendements trimestriels
rendements_trimestriels = data_dassault_modifie.groupby(['Année', 'Trimestre'])['Taux de Variation Mensuelle'].apply(
    lambda x: (1 + x).prod() - 1).reset_index(name='Rendement Trimestriel')

# Calculer les rendements annuels
rendements_annuels = data_dassault_modifie.groupby('Année')['Taux de Variation Mensuelle'].apply(
    lambda x: (1 + x).prod() - 1).reset_index(name='Rendement Annuel')

# Afficher les résultats
print("Rendements trimestriels de l'action Dassault :")
print(rendements_trimestriels)

print("\nRendements annuels de l'action Dassault :")
print(rendements_annuels)

chemin_fichier_trimestriels = 'Taux/rendements_trimestriels_dassault.csv'
chemin_fichier_annuels = 'Taux/rendements_annuels_dassault.csv'

# Sauvegarder les rendements trimestriels dans un fichier CSV
rendements_trimestriels.to_csv(chemin_fichier_trimestriels, index=False, sep=';')

# Sauvegarder les rendements annuels dans un autre fichier CSV
rendements_annuels.to_csv(chemin_fichier_annuels, index=False, sep=';')

print(f"Les rendements trimestriels ont été sauvegardés dans : {chemin_fichier_trimestriels}")
print(f"Les rendements annuels ont été sauvegardés dans : {chemin_fichier_annuels}")
