# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df
# %%
df.shape
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
renamed_columns = {
    "QtdePontos": "qtPontos",
    "DescSistemaOrigem": "SistemaOrigem"
}
# %%
df.rename(columns=renamed_columns, inplace=True)
df

# %%
colunas = ["IdCliente", "qtPontos"]
df[colunas]
# %%

# SELELECT IdCliente FROM df

df[["IdCliente"]]
# %%

# SELECT IdCliente, qtPontos FROM df LIMIT 5

df[["IdCliente", "qtPontos"]].head(5)

df[["IdCliente", "qtPontos"]].tail(5)

df[["IdCliente", "qtPontos"]].sample(5)
# %%

# SELECT IdCliente, IdTransacao, qtPontos
# FROM df
# LIMIT 5

df[["IdCliente", "IdTransacao", "qtPontos"]].head(5)
# %%
#Como deixar as colunas em ordem alfabetica.
colunas = df.columns.tolist()
colunas.sort()
colunas
# %%

df = df[colunas]
df
# %%
