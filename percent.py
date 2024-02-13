import pandas as pd
import os
import matplotlib.pyplot as plt
df_actif = pd.read_csv("Actifs_df/Actifcsv_df_dassault", delimiter=";")

print(type(df_actif))
df_actif['Date'] = pd.to_datetime(df_actif['Date'])
"""annee_spec = 2011
data_filtree = df_actif[df_actif['Date'].dt.year == annee_spec]
valeur_initiale = data_filtree.iloc[0]['Taux de Variation Mensuelle']
valeur_finale = data_filtree.iloc[-1]['Taux de Variation Mensuelle']

taux_variation_annuelle = ((valeur_finale - valeur_initiale) / valeur_initiale) * 100

# Ajouter le taux de variation annuelle comme une nouvelle colonne, ici on remplira avec la même valeur pour simplification
df_actif['Taux de variation annuelle'] = None  # Initialiser avec None ou une valeur par défaut
df_actif.loc[df_actif['Date'].dt.year == annee_spec, 'Taux de variation annuelle'] = taux_variation_annuelle.round(2)

# Afficher les types de données

print(df_actif.head(25))"""

resultat = []

for name, group in df_actif.groupby(df_actif["Date"].dt.year):
    if group['Taux de Variation Mensuelle'].empty:
        continue
    valeur_initial = group.iloc[0]['Taux de Variation Mensuelle']
    valeur_final = group.iloc[-1]['Taux de Variation Mensuelle']
    taux_variation_annuelle = ((valeur_final - valeur_initial) * 100 if valeur_initial != 0 else 0)

    resultat.append({'Année': name, 'Taux de Variation Annuelle': round(taux_variation_annuelle, 2)})

resultat = pd.DataFrame(resultat)

print(resultat)

nouveau_fichier = "Taux_variation_annuelle/Variation_df_dassault.csv"

if os.path.exists(nouveau_fichier):
    print("Le fichier existe déjà")
else:
    resultat.to_csv(nouveau_fichier, sep=';', encoding='utf-8', index=False)
    print(f"Le fichier a été créé avec succès à l'emplacement : {nouveau_fichier}")


plt.plot(resultat["Année"],resultat["Taux de Variation Annuelle"])
plt.title("Taux de Variation annuelle depuis 2011")
plt.xlabel("Année")
plt.ylabel("Taux de Variation annuelle")
plt.show()