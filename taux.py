import pandas as pd

# Étape 1: Charger les données
from charge_dossier_csv import charger_csv_dossier

# Charger les données
dossier = "Actifs_modifie"
dataframes = charger_csv_dossier(dossier)

for nom_fichier, dataframe in dataframes.items():
    # Extraire le nom de l'entreprise à partir du nom du fichier
    nom_entreprise = nom_fichier.split('Actif_')[-1].split('_modifie')[0].capitalize()

    # Convertir la colonne 'Date' en datetime pour faciliter le regroupement
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], dayfirst=True)

    # Définir l'année et le trimestre pour chaque ligne
    dataframe['Année'] = dataframe['Date'].dt.year
    dataframe['Trimestre'] = dataframe['Date'].dt.to_period('Q')

    # Calculer les rendements trimestriels
    rendements_trimestriels = dataframe.groupby(['Année', 'Trimestre'])['Taux de Variation Mensuelle'].apply(
        lambda x: (1 + x).prod() - 1).reset_index(name='Rendement Trimestriel')

    # Calculer les rendements annuels
    rendements_annuels = dataframe.groupby('Année')['Taux de Variation Mensuelle'].apply(
        lambda x: (1 + x).prod() - 1).reset_index(name='Rendement Annuel')

    # Afficher les résultats
    print(f"Rendements trimestriels de l'action {nom_entreprise} :")
    print(rendements_trimestriels)

    print(f"\nRendements annuels de l'action {nom_entreprise} :")
    print(rendements_annuels)

    chemin_fichier_trimestriels = f'Taux/{nom_entreprise}/rendements_trimestriels_{nom_entreprise}.csv'
    chemin_fichier_annuels = f'Taux/{nom_entreprise}/rendements_annuels_{nom_entreprise}.csv'

    # Sauvegarder les rendements trimestriels dans un fichier CSV
    rendements_trimestriels.to_csv(chemin_fichier_trimestriels, index=False, sep=';')

    # Sauvegarder les rendements annuels dans un autre fichier CSV
    rendements_annuels.to_csv(chemin_fichier_annuels, index=False, sep=';')

    print(f"Les rendements trimestriels ont été sauvegardés dans : {chemin_fichier_trimestriels}")
    print(f"Les rendements annuels ont été sauvegardés dans : {chemin_fichier_annuels}")
