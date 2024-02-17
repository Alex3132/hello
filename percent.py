import pandas as pd
import os
import matplotlib.pyplot as plt

df_actif = pd.read_csv("Actifs_df/Actif_dassault_modifie.csv", delimiter=";")

print(type(df_actif))

"""
Taux de variation trimestriel
"""
# Assurez-vous que 'Date' est au format datetime
df_actif["Date"] = pd.to_datetime(df_actif["Date"])

print(type(df_actif["Date"]))
# Convertir les dates en périodes trimestrielles

df_actif['Date_trimestre_debut'] = df_actif['trimestres_année'].dt.to_timestamp()

# Afficher le résultat
print(df_actif['Date_trimestre_debut'])

# Regrouper les données par trimestre et calculer le taux de variation trimestrielle
df_grouped = df_actif.groupby('trimestres_année')['Taux de Variation Mensuelle'].sum().reset_index()

print(df_grouped)
# Renommer la colonne de somme pour refléter qu'elle représente le taux de variation trimestrielle
df_grouped.rename(columns={'Taux de Variation Mensuelle': 'taux de variation trimestrielle'}, inplace=True)

# Pour s'assurer que tous les trimestres sont représentés, même ceux sans données :
# Créer une série de tous les trimestres entre le premier et le dernier enregistrement
all_quarters = pd.period_range(start=df_actif['trimestres_année'].min(), end=df_actif['trimestres_année'].max(),
                               freq='Q')
print(all_quarters)
# Créer un DataFrame vide avec tous les trimestres
df_all_quarters = pd.DataFrame(all_quarters, columns=['trimestres_année'])

# Fusionner avec les données calculées, en remplissant les valeurs manquantes par 0
df_final = pd.merge(df_all_quarters, df_grouped, how='left', on='trimestres_année')
df_final['taux de variation trimestrielle'] = df_final['taux de variation trimestrielle'].round(4)

# Affichage pour vérification
print(df_final.head())

# Enregistrement du résultat final, ajustez le chemin selon vos besoins
df_final.to_csv('Taux_variation_trimestrielle.csv', index=False, sep=';')
"""
# Calculer le taux de variation trimestrielle
df_taux_variation = df_actif.groupby('trimestres_année')['Taux de Variation Mensuelle'].sum().round(4).reset_index()
df_taux_variation.rename(columns={'Taux de Variation Mensuelle': 'taux de variation trimestrielle'}, inplace=True)

# Si nécessaire, créer une plage de tous les trimestres entre la première et la dernière date
min_date, max_date = df_actif['Date'].min(), df_actif['Date'].max()
all_quarters = pd.period_range(min_date, max_date, freq='Q')

# Assurer la présence de tous les trimestres dans le résultat final
df_taux_variation['trimestres_année'] = pd.PeriodIndex(df_taux_variation['trimestres_année'])
df_all_quarters = pd.DataFrame(all_quarters, columns=['trimestres_année'])
df_final = pd.merge(df_all_quarters, df_taux_variation, on='trimestres_année', how='left').fillna(0)
"""
# Afficher ou sauvegarder le résultat final
# print(df_final)
# Si nécessaire, sauvegarder dans un fichier CSV
# df_final.to_csv('Taux_variation_trimestrielle/Variation_df_dassault.csv', index=False, sep=';')
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

volume = []
for name, group in df_actif.groupby(df_actif["Date"].dt.year):
    if group['Volume'].empty:
        continue

    # Calculer le volume total pour l'année
    volume_total_annuel = group['Volume'].sum()

    # Trouver le nombre de mois uniques dans l'année
    nombre_de_mois = group['Date'].dt.month.nunique()

    # Calculer le volume moyen par mois pour l'année
    volume_moyen_par_mois = volume_total_annuel / nombre_de_mois if nombre_de_mois > 0 else 0

    volume.append({'Année': name, 'Volume_Moyen_Par_Mois': round(volume_moyen_par_mois, 2)})

volume = pd.DataFrame(volume)

print(volume)

#########################################################################

nouveau_fichier = "Taux_variation_annuelle/Variation_df_dassault.csv"

if os.path.exists(nouveau_fichier):
    print("Le fichier existe déjà")
else:
    resultat.to_csv(nouveau_fichier, sep=';', encoding='utf-8', index=False)
    print(f"Le fichier a été créé avec succès à l'emplacement : {nouveau_fichier}")

"""plt.plot(resultat["Année"],resultat["Taux de Variation Annuelle"])
plt.title("Taux de Variation annuelle depuis 2011")
plt.xlabel("Année")
plt.ylabel("Taux de Variation annuelle")
plt.show()"""

plt.plot(volume["Année"], volume["Volume_Moyen_Par_Mois"])
plt.title("Moyenne de volume annuelle depuis 2011")
plt.xlabel("Année")
plt.ylabel("Moyenne de volume")
plt.show()
