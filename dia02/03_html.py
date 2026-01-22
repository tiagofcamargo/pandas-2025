# %%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}

html = requests.get(url, headers=headers).text
dfs = pd.read_html(html)  # agora lê a string HTML
dfs

# %%

df_uf = dfs[1]
df_uf.to_csv("ufs.csv", sep=";", index=False)
# %%
