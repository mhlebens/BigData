import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder

#1 Cargar el dataset
df = pd.read_csv("sample_data/EscuelaTech.csv")
print("DataFrame original:")
display(df.head())

#2 Gestionar variables categóricas (Label Enconding)
for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col]= le.fit_transform(df[col])

#3 Centralizar los datos
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols] - df[numeric_cols].mean()
display(df.head())

#4 Estandarizar los datos
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
display(df.head())

#5 Identificar y limpiar atípicos usando IQR
Q1 = df[numeric_cols].quantile(0.25)
Q3 = df[numeric_cols].quantile(0.75)
IQR = Q3 - Q1
df_cleaned = df[~((df[numeric_cols] < (Q1 - 1.5 * IQR)) )]