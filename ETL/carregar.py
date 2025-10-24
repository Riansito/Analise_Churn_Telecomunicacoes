import pandas as pd

def carregar_para_excel(lista_tabelas, nomes_abas):
    #Carrega as tabelas criadas para o arquivo excel
    with pd.ExcelWriter("Dados/clientes_churn.xlsx", engine="xlsxwriter") as writer:
        for tabela, nome in zip(lista_tabelas, nomes_abas):
            tabela.to_excel(writer, sheet_name = nome, index = False)

        