
from ETL.extrair import extrair_dados_csv
from ETL.transformar import *
from ETL.carregar import carregar_para_excel

if __name__ == "__main__":
    """
    Executa o pipeline completo de ETL.
    """
    # Extração
    df = extrair_dados_csv("Dados/mtn_customer_churn.csv")

    # Transformação
    dim_clientes, dim_dispositivos_mtn, dim_planos_assinaturas, fat_vendas = transformar(df)

    lista_tabelas = [dim_clientes, dim_dispositivos_mtn, dim_planos_assinaturas, fat_vendas]
    nomes_abas = ["dim_clientes", "dim_dispositivos_mtn", "dim_planos_assinaturas", "fat_vendas"]

    # Carga

    carregar_para_excel(lista_tabelas, nomes_abas)

    print("🎯 Pipeline ETL finalizado com sucesso!")
  
