import pandas as pd

df_actif = pd.read_csv("Actifs_df/Actifcsv_df_dassault", delimiter=";")

print(df_actif.head())