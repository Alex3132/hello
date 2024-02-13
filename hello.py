import pandas as pd
import os

data = pd.read_csv("Actifs/Actifcsv.csv", delimiter=";")
data["Date"] = pd.to_datetime(data["Date"])
data['Volume'] = data['Volume'].str.replace(' ', '').replace(',', '').astype(int)
data["Entreprise"] = "Dassault"
data['Entreprise'] = data['Entreprise'].astype(str)
data = data.drop(columns=["Taux de Variation Trimestrielle", "Taux de Variation Annuelle"])
data.iloc[:, 7:11] = data.iloc[:, 7:11].apply(lambda x: x.round(4))


type_data = data.dtypes

print(data["Covarience Actif marché"].head())

nouveau_fichier = "Actifs_df/Actifcsv_df_dassault"

if os.path.exists(nouveau_fichier):
    print("Le fichier existe déjà")
else:
    data.to_csv(nouveau_fichier, sep=';', encoding='utf-8', index=False)
    print(f"Le fichier a été créé avec succès à l'emplacement : {nouveau_fichier}")
