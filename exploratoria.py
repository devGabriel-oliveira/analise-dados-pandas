import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn")

df = pd.read_excel("AdventureWorks.xlsx")

df.head()
df.shape


#Qual a Receita total?
df["Valor Venda"].sum()

#Qual o custo Total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna de custo

#Qual o custo Total?
round(df["custo"].sum(), 2)

#Agora que temos a receita e custo e o total, podemos achar o Lucro total

#Vamos criar uma coluna de Lucro que será Receita - Custo
df["lucro"]  = df["Valor Venda"] - df["custo"] 


#Total Lucro
round(df["lucro"].sum(),2)

#Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]


df.head(1)

#Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
     

df.head(1)


#Verificando o tipo da coluna Tempo_envio
df["Tempo_envio"].dtype


#Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()

#Verificando se temos dados faltantes
df.isnull().sum()
     
#E, se a gente quiser saber o Lucro por Ano e Por Marca?


#Vamos Agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

#Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#Gráfico Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
df_2009.head()


df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')

df["Tempo_envio"].describe()

#Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"])

#Histograma
plt.hist(df["Tempo_envio"])

#Tempo mínimo de envio
df["Tempo_envio"].min()

#Tempo máximo de envio
df['Tempo_envio'].max()

#Identificando o Outlier
df[df["Tempo_envio"] == 20]

df.to_csv("df_vendas_novo.csv", index=False)