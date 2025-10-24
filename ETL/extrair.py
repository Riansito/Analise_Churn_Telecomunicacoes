import pandas as pd

def extrair_dados_csv(caminho: str) -> pd.DataFrame:
    #Retorna os dados dos clientes
    return pd.read_csv(caminho)