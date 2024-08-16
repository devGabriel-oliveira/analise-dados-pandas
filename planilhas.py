import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df = pd.concat([df1,df2,df3,df4,df5])

#print(df.sample(3))

# Alterando o tipo de dado de cada coluna 
#df["LojaID"] = df["LojaID"].astype("object")

#print(df.dtypes)

#print(df.isnull().sum())

# CRIANDO COLUNA RECEITAS

df["Receita"] = df["Vendas"].mul(df["Qtde"])
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# // TRANSFORMANDO OS DADOS / DATAS

#df["Data"] = pd.to_datetime(df["Data"], errors='coerce')

#Agrupamento // Receita por ano


#receita_por_ano = df.groupby(df["Data"].dt.year)["Receita"].sum()
#print(receita_por_ano)


# // CRIANDO COLUNA COM O ANO 
#df["Ano_Venda"] = df["Data"].dt.year

#print(df.sample(10))

#  // GERANDO GRÁFICOS

#print(df["LojaID"].value_counts(ascending=False))

#print(df["LojaID"].value_counts().plot.barh())

df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()
df["Cidade"].value_counts()

plt.show()
