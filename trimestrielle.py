import warnings

warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

import pandas as pd


df_actif = pd.read_csv("Actifs_df/Actif_dassault_modifie.csv", delimiter=";")

print(type(df_actif))

test = df_actif[['Date',"Taux de Variation Mensuelle"]].copy()

print(test)

test['Date'] = pd.to_datetime(test['Date'],format='%d/%m/%Y')
print(test["Date"])
# Créer une colonne 'trimestre_année' pour représenter le trimestre et l'année
test['trimestre_année'] = test['Date'].dt.to_period('Q')

# Calculer le taux de variation trimestrielle
# Remplacez 'sum' par 'mean' si vous préférez calculer la moyenne plutôt que la somme
taux_variation_trimestrielle = test.groupby('trimestre_année')['Taux de Variation Mensuelle'].sum().reset_index()

# Renommer la colonne pour refléter le calcul effectué
taux_variation_trimestrielle.rename(columns={'Taux de Variation Mensuelle': 'taux de variation trimestrielle'}, inplace=True)

# Afficher le résultat
print(taux_variation_trimestrielle)
type_data = df_actif.dtypes
print(type_data)
