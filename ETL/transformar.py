import pandas as pd

# =========================================================
# ⚙️ ETAPA 2 - TRANSFORMAÇÃO COMPLETA
# =========================================================
def traduzir_colunas(df: pd.DataFrame) -> pd.DataFrame:
    colunas_traduzidas = {
        "Customer ID": "ID do Cliente",
        "Full Name": "Nome Completo",
        "Date of Purchase": "Data da Compra",
        "Age": "Idade",
        "State": "Estado",
        "MTN Device": "Dispositivo MTN",
        "Gender": "Gênero",
        "Satisfaction Rate": "Taxa de Satisfação",
        "Customer Review": "Avaliação do Cliente",
        "Customer Tenure in months": "Tempo de Cliente (meses)",
        "Subscription Plan": "Plano de Assinatura",
        "Unit Price": "Preço Unitário",
        "Number of Times Purchased": "Número de Compras",
        "Total Revenue": "Receita Total",
        "Data Usage": "Uso de Dados",
        "Customer Churn Status": "Status de Cancelamento",
        "Reasons for Churn": "Motivos do Cancelamento"
    }
    df.rename(columns = colunas_traduzidas, inplace=True)
    return df


def traduzir_valores_colunas(dataset: pd.DataFrame, dicionario_maps: dict) -> pd.DataFrame:
    for coluna, mapa in dicionario_maps.items():
        if coluna in dataset.columns:
            dataset[coluna] = dataset[coluna].map(mapa)
    return dataset

def aplicar_traducoes(df: pd.DataFrame) -> pd.DataFrame:
    
    #Mudando valores
    status_de_cancelamento_dict = {
        "Yes" : 1,
        "No" : 0
    }
    
    #Tradução para o 'Gênero'
    genero_dict = {
        "Male" : "Masculino",
        "Female" : "Feminino"
    }
    # Tradução para 'Dispositivo MTN'
    dispositivo_mtn_dict = {
        "Mobile SIM Card": "Chip Móvel",
        "5G Broadband Router": "Roteador 5G",
        "Broadband MiFi": "MiFi Banda Larga",
        "4G Router": "Roteador 4G"
    }

    # Tradução para 'Avaliação do Cliente'
    avaliacao_cliente_dict = {
        "Very Good": "Muito Bom",
        "Fair": "Regular",
        "Good": "Bom",
        "Poor": "Ruim",
        "Excellent": "Excelente"
    }

    # Tradução para 'Plano de Assinatura'
    plano_assinatura_dict = {
        "60GB Monthly Broadband Plan": "Plano Mensal 60GB",
        "150GB FUP Monthly Unlimited": "Plano Mensal 150GB Ilimitado FUP",
        "30GB Monthly Broadband Plan": "Plano Mensal 30GB",
        "165GB Monthly Plan": "Plano Mensal 165GB",
        "300GB FUP Monthly Unlimited": "Plano Mensal 300GB Ilimitado FUP",
        "120GB Monthly Broadband Plan": "Plano Mensal 120GB",
        "10GB+10mins Monthly Plan": "Plano Mensal 10GB + 10min",
        "65GB Monthly Plan": "Plano Mensal 65GB",
        "25GB Monthly Plan": "Plano Mensal 25GB",
        "12.5GB Monthly Plan": "Plano Mensal 12,5GB",
        "3.2GB 2-Day Plan": "Plano 2 Dias 3,2GB",
        "200GB Monthly Broadband Plan": "Plano Mensal 200GB",
        "2.5GB 2-Day Plan": "Plano 2 Dias 2,5GB",
        "16.5GB+10mins Monthly Plan": "Plano Mensal 16,5GB + 10min",
        "500MB Daily Plan": "Plano Diário 500MB",
        "1.5GB 2-Day Plan": "Plano 2 Dias 1,5GB",
        "7GB Monthly Plan": "Plano Mensal 7GB",
        "1.5TB Yearly Broadband Plan": "Plano Anual 1,5TB",
        "450GB 3-Month Broadband Plan": "Plano Trimestral 450GB",
        "1GB+1.5mins Daily Plan": "Plano Diário 1GB + 1,5min",
        "20GB Monthly Plan": "Plano Mensal 20GB"
    }

    # Tradução para 'Motivos do Cancelamento'
    motivos_cancelamento_dict = {
        "High Call Tarriffs": "Tarifas de Chamada Altas",
        "Better Offers from Competitors": "Melhores Ofertas de Concorrentes",
        "Poor Network": "Rede Ruim",
        "Costly Data Plans": "Planos de Dados Caros",
        "Poor Customer Service": "Atendimento Ruim",
        "Fast Data Consumption": "Consumo Rápido de Dados",
        "Relocation": "Mudança de Local"
    }

    dicionario_maps ={
        "Gênero" : genero_dict,
        'Dispositivo MTN' : dispositivo_mtn_dict,
        'Avaliação do Cliente' : avaliacao_cliente_dict,
        'Plano de Assinatura' : plano_assinatura_dict,
        'Motivos do Cancelamento':motivos_cancelamento_dict,
        'Status de Cancelamento': status_de_cancelamento_dict
    }
    return traduzir_valores_colunas(df, dicionario_maps)

def criar_ids_dimensao(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria os IDs das dimensões e retorna o df
    """
    # Dimensões
    df['ID Dispositivo MTN'] = df['Dispositivo MTN'].factorize()[0] + 1
    df['ID Plano de Assinatura'] = df['Plano de Assinatura'].factorize()[0] + 1
    df['ID Plano de Assinatura'] = df['Plano de Assinatura'].factorize()[0] + 1

    return df

#Modelagem dos dados
def criar_tabelas_dimensao(df: pd.DataFrame) -> pd.DataFrame:
    dim_clientes = df[['ID do Cliente', 'Nome Completo', 'Idade', 'Estado', 'Gênero']].drop_duplicates().reset_index(drop=True)
    dim_dispositivos_mtn = df[['ID Dispositivo MTN', 'Dispositivo MTN']].drop_duplicates().reset_index(drop=True)
    dim_planos_assinaturas = df[['ID Plano de Assinatura', 'Plano de Assinatura', 'Preço Unitário']].drop_duplicates().reset_index(drop=True)
    return dim_clientes, dim_dispositivos_mtn, dim_planos_assinaturas

def criar_tabela_fato(df: pd.DataFrame, colunas_remover):
    fat_vendas = df.drop(columns=colunas_remover, axis=1)
    return fat_vendas


def transformar(df: pd.DataFrame):
    """
    Pipeline completo de transformação e criação de dimensões/fato
    Corrige o uso dos IDs nas tabelas fato.
    """
    print("⚙️ Transformando dados...")

    # Traduzir colunas e valores
    df = traduzir_colunas(df)
    print("Tradução das colunas encerradas!")

    df = aplicar_traducoes(df)
    print("Tradução dos valores das colunas encerradas!")

    # Criar IDs das dimensões
    df = criar_ids_dimensao(df)
    print("ID's criados com sucessos")

    # Criar dimensões
    dim_clientes, dim_dispositivos_mtn, dim_planos_assinaturas = criar_tabelas_dimensao(df)

    colunas_remover = ['Nome Completo', 'Idade', 'Estado', 'Gênero', 'Dispositivo MTN', 'Plano de Assinatura', 'Preço Unitário']
    # Criar tabela fato
    fat_vendas = criar_tabela_fato(df, colunas_remover)

    print("✅ Transformação concluída!")
    return dim_clientes, dim_dispositivos_mtn, dim_planos_assinaturas, fat_vendas