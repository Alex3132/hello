import pandas as pd
from charge_dossier_csv import charger_csv_dossier

# Charger les données
dossier = "Actifs_modifie"
dataframes = charger_csv_dossier(dossier)

for nom_fichier in dataframes:
    chemin_complet = f"{dossier}/{nom_fichier}"
    data = pd.read_csv(chemin_complet, delimiter=';')
# Convertir la colonne 'Date' en datetime si nécessaire pour d'autres analyses
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    
    # étape 2 : Calculer le bêta de l'action Dassault
    # Calcul de la moyenne de la covariance entre l'actif et le marche et de la variance du marché
    moyenne_covariance = data['Covarience Actif marché'].mean()
    moyenne_variance_marche = data['Variance de la rentabilité du marché'].mean()
    
    # Calcul du bêta de l'action Dassault
    beta_entreprise = moyenne_covariance / moyenne_variance_marche
    nom_entreprise = nom_fichier.split('Actif_')[-1].split('_modifie')[0].capitalize()
    
    # Afficher les resultats
    print(f"Moyenne de la covariance entre les rendements de l'action {nom_entreprise} et ceux du marche: {moyenne_covariance}")
    print(f"Moyenne de la variance des rendements du marche: {moyenne_variance_marche}")
    print(f"Bêta de l'action {nom_entreprise}: {beta_entreprise}")
    
    # etape 3: Interpreter le bêta
    if beta_entreprise > 1:
        print(f"L'action {nom_entreprise} est plus volatile que le marche global.")
    elif beta_entreprise < 1:
        print(f"L'action {nom_entreprise} est moins volatile que le marche global.")
    else:
        print(f"La volatilité de l'action {nom_entreprise} est équivalente à celle du marche global.")
