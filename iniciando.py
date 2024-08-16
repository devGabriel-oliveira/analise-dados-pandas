import pandas as pd

# Use o delimitador correto para ler o CSV, caso esteja separado por ponto e vírgula
df = pd.read_csv("C:\\Users\\Usuário\\Desktop\\Curso Python\\DIO\\Pandas\\gampyder.csv", delimiter=';')


df = df.rename(columns={"country": "Pais", "continent": "continente", "year": "Ano", "lifeExp": "Expectativa de vida", "pop": "Pop Total", "gdpPercap": "PIB"})

#Saber Total de linhas e colunas
# df.shape

#nome das colunas
#df.columns

# ultimas linhas da tabela
# df.tail

# retorna info sobre os dados
# df.describe()

# oegar as colunas que quero com valores unicos
# df["continente"].unique()

# print(df["continente"].unique())

#Oceania = df.loc[df["continente"] == "Oceania"]
# print(Oceania.head())


#print(df.groupby("continente")["Pais"].nunique())

print(df.groupby("Ano")["Expectativa de vida"].mean())


