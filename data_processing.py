import pandas as pd
import os

dossier = "Actifs"
fichiers = os.listdir(dossier)

for nom_fichier in fichiers:
    chemin_complet = f"{dossier}/{nom_fichier}"
    data = pd.read_csv(chemin_complet, delimiter=";")
    data.fillna(0.0, inplace=True)
    # modification des données pour etre plus lisible
    data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
    data['Volume'] = data['Volume'].str.replace(' ', '').replace(',', '').astype(int)
    nom_entreprise = nom_fichier.split("_")[1].split(".")[0].capitalize()
    data["Entreprise"] = nom_entreprise

    data = data.drop(columns=["Taux de Variation Trimestrielle", "Taux de Variation Annuelle"])
    data.iloc[:, 7:11] = data.iloc[:, 7:11].apply(lambda x: x.round(4))

    # verification des modifs
    type_data = data.dtypes
    print(type_data)

    # Sauvegardez le DataFrame modifié
    nom_fichier_modifie = nom_fichier.replace(".csv", "_modifie.csv")
    chemin_sauvegarde = f"{dossier}_df/{nom_fichier_modifie}"

    if not os.path.exists(chemin_sauvegarde):
        data.to_csv(chemin_sauvegarde, index=False, sep=";", encoding='utf-8', date_format='%d/%m/%Y')
    else:
        print(f"Le fichier {nom_fichier_modifie} existe déjà.")
