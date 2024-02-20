import pandas as pd
import numpy as np

# etape 1: Charger les donnees
file_path_dassault = 'Actifs_df/Actif_dassault_modifie.csv'  # Chemin d'accès au fichier telecharge
data_dassault = pd.read_csv(file_path_dassault, delimiter=';')

# Convertir la colonne 'Date' en datetime si necessaire pour d'autres analyses
data_dassault['Date'] = pd.to_datetime(data_dassault['Date'], dayfirst=True)

# etape 2: Calculer le bêta de l'action Dassault
# Calcul de la moyenne de la covariance entre l'actif et le marche et de la variance du marché
moyenne_covariance = data_dassault['Covarience Actif marché'].mean()
moyenne_variance_marche = data_dassault['Variance de la rentabilité du marché'].mean()

# Calcul du bêta de l'action Dassault
beta_dassault = moyenne_covariance / moyenne_variance_marche

# Afficher les resultats
print(f"Moyenne de la covariance entre les rendements de l'action Dassault et ceux du marche: {moyenne_covariance}")
print(f"Moyenne de la variance des rendements du marche: {moyenne_variance_marche}")
print(f"Bêta de l'action Dassault: {beta_dassault}")

# etape 3: Interpreter le bêta
if beta_dassault > 1:
    print("L'action Dassault est plus volatile que le marche global.")
elif beta_dassault < 1:
    print("L'action Dassault est moins volatile que le marche global.")
else:
    print("La volatilite de l'action Dassault est equivalente à celle du marche global.")
