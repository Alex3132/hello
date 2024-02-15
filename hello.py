import pandas as pd
import os

dossier = "Actifs"
fichiers = os.listdir(dossier)

for nom_fichier in fichiers:
    chemin_complet = f"{dossier}/{nom_fichier}"
    data = pd.read_csv(chemin_complet, delimiter=";")
    # modification des données pour etre plus lisible
    data["Date"] = pd.to_datetime(data["Date"])
    data['Volume'] = data['Volume'].str.replace(' ', '').replace(',', '').astype(int)
    data["Entreprise"] = "Dassault"
    data['Entreprise'] = data['Entreprise'].astype(str)
    data = data.drop(columns=["Taux de Variation Trimestrielle", "Taux de Variation Annuelle"])
    data.iloc[:, 7:11] = data.iloc[:, 7:11].apply(lambda x: x.round(4))
    # verification des modifs
    type_data = data.dtypes
    print(type_data)

    # Sauvegardez le DataFrame modifié
    nom_fichier_modifie = nom_fichier.replace(".csv", "_modifie.csv")
    chemin_sauvegarde = f"{dossier}_df/{nom_fichier_modifie}"
    data.to_csv(chemin_sauvegarde, index=False)

    chemin_sauvegarde = f"{dossier}_df/{nom_fichier_modifie}"

    if not os.path.exists(chemin_sauvegarde):
        data.to_csv(chemin_sauvegarde, index=False)
    else:
        print(f"Le fichier {nom_fichier_modifie} existe déjà.")

# data = pd.read_csv("Actifs/Actifcsv.csv", delimiter=";")

# autre solution pour convertir des chaines en nombre
"""colonnes_a_convertir = ['Colonne1', 'Colonne2', 'Colonne3']

for colonne in colonnes_a_convertir:
    # Enlever le symbole "€" et les virgules, puis convertir en float
    data[colonne] = data[colonne].str.replace('€', '').str.replace(',', '.').astype(float)"""

"""# modification des données pour etre plus lisible
data["Date"] = pd.to_datetime(data["Date"])
data['Volume'] = data['Volume'].str.replace(' ', '').replace(',', '').astype(int)
data["Entreprise"] = "Dassault"
data['Entreprise'] = data['Entreprise'].astype(str)
data = data.drop(columns=["Taux de Variation Trimestrielle", "Taux de Variation Annuelle"])
data.iloc[:, 7:11] = data.iloc[:, 7:11].apply(lambda x: x.round(4))"""

"""# verification des modifs
type_data = data.dtypes

print(type_data)

# création d'un nouveau fichier

nouveau_fichier = "Actifs_df/Actifcsv_df_dassault"

if os.path.exists(nouveau_fichier):
    print("Le fichier existe déjà")
else:
    data.to_csv(nouveau_fichier, sep=';', encoding='utf-8', index=False)
    print(f"Le fichier a été créé avec succès à l'emplacement : {nouveau_fichier}")"""
