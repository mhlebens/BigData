import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
 
 
df = pd.read_csv("Semana10/FOOD_DATA_GROUP.csv")
 
 
print(df.head)
print(df.info())
 
 
print(df["Calories"].describe())
 
 
print(df["Food_Group"].value_counts())
 
 
# plt.hist(df["Calories"], bins=10)
 
 
# plt.title("Distribucion de Calories")
# plt.xlabel("Calories")
# plt.ylabel("Cantidad")
# plt.show()
 
 
 
# plt.boxplot(df["Calories"])
# plt.title("boxplot de Calories")
# plt.show()
 
 
 
# plt.scatter(df["Calories"], df["Protein_g"])
# plt.xlabel("Protein_g")
# plt.ylabel("Calories")
# plt.show()
 
 
 
df["CaloriasDistribucion"] = pd.cut(
    df["Calories"],
    bins=[0, 150, 300, 600],
    labels=["Bajas 150", "Medias 300", "Altas 600"]
)
 
print(df["CaloriasDistribucion"].value_counts())
 
 
train, test =  train_test_split(
    df,
    test_size=0.20,
    random_state=42,
    stratify=df["Food_Group"]
)
 
 
train2, test2 =  train_test_split(
    df,
    test_size=0.30,
    random_state=42,
    stratify=df["Food_Group"]
)
 
 
print("train: ", train.shape)
print("test: ", test.shape)
 
 
print("Original")
print(df["Food_Group"].value_counts(normalize=True))
 
print("\ntrain")
print(train["Food_Group"].value_counts(normalize=True))
 
print("\ntrain2")
print(train2["Food_Group"].value_counts(normalize=True))