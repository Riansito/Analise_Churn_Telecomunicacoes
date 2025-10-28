

# 📉 Análise de Churn — Empresa de Telecomunicações

## 📘 **Introdução**

O churn (ou taxa de cancelamento) é um dos principais desafios enfrentados por empresas que trabalham com assinaturas e planos de serviço.
Compreender **por que clientes estão cancelando** e **quais produtos ou planos estão mais propensos a isso** é essencial para desenvolver estratégias de retenção eficazes.

Este projeto tem como objetivo **analisar os padrões de churn de uma empresa de telecomunicações**, identificando:

* Quais dispositivos e planos apresentam mais cancelamentos;
* Quais motivos estão associados ao churn;
* E como essas variáveis impactam a receita e o desempenho da empresa ao longo do tempo.

---

## ❗ **Problema de Negócio**

O **churn de clientes** é uma das maiores preocupações de empresas de telecomunicações — especialmente em **mercados competitivos**, como o da **Nigéria**.

O dataset utilizado neste projeto **mostra o comportamento, preferências e padrões de cancelamento dos clientes da MTN Nigeria no 1º trimestre de 2025**.

A empresa vinha observando **aumento no número de cancelamentos** e **queda na rentabilidade** em alguns produtos.
O desafio foi **descobrir quais produtos e planos mais contribuíam para o churn** e **quais fatores estavam levando os clientes a desistirem do serviço**.

## ⚙️ **Etapas do Projeto (Processo ETL)**

### **1. Extração dos Dados (Extract)**

Os dados foram coletados a partir de diferentes fontes de cadastro e histórico de clientes da empresa, contendo informações como:

* ID do cliente,
* Data da compra,
* Tipo de dispositivo,
* Plano de assinatura,
* Receita total,
* Status de cancelamento e motivo do churn.

---

### **2. Transformação dos Dados (Transform)**

Durante a etapa de tratamento, foi realizado um trabalho detalhado de limpeza e padronização com **Python e Pandas**:

* Tradução dos nomes de colunas e valores para o português;
* Criação de **IDs únicos** para os planos e dispositivos;
* Separação do dataset em **tabelas fato** e **tabelas dimensão** (seguindo o modelo estrela).

Essa modelagem foi fundamental para facilitar a análise posterior no Excel Power Pivot.

---

### **3. Carga dos Dados (Load)**

Após o tratamento, os dados foram exportados e carregados no **Excel**, onde foram criados:

* Modelos relacionais com **Power Pivot**;
* **Tabelas dinâmicas** para análises descritivas;
* **Gráficos dinâmicos** para visualização dos resultados.

A modelagem permitiu explorar diferentes perspectivas (por dispositivo, plano, motivo e período).

---

## 🧩 **Modelagem dos Dados**

A modelagem foi realizada no **Power Pivot**, seguindo o **modelo estrela (Star Schema)**, permitindo uma análise eficiente e relacional.

As tabelas foram estruturadas da seguinte forma:

### **Tabelas Dimensão (Dim)**

* **Dim_Clientes** → Contém informações como ID do cliente, tempo de cliente e taxa de satisfação.
* **Dim_DispositivosMTN** → Contém os tipos de dispositivos comercializados (ex: Chip Móvel, Modem, Roteador etc.).
* **Dim_Planos** → Contém os detalhes dos planos de assinatura, como nome, tipo e franquia de dados.

### **Tabela Fato (Fat)**

* **Fat_Churn** → Contém os registros de cancelamento, integrando IDs das dimensões (cliente, dispositivo e plano), além das métricas de negócio como:

  * Status de cancelamento,
  * Receita total,
  * Uso de dados,
  * Motivo do cancelamento,
  * Data da compra.

Essa modelagem permitiu criar **medidas DAX** e **relacionamentos entre tabelas**, otimizando as análises no Power Pivot e garantindo maior flexibilidade nas explorações via tabelas e gráficos dinâmicos.

*Modelagem dos Dados*
<img width="1917" height="1018" alt="modelagem_dados" src="https://github.com/user-attachments/assets/9db7f9ca-43e4-4eec-b64d-c05df4d2572f" />

---

## 🧰 **Tecnologias Utilizadas**

| Tecnologia                                               | Finalidade                                    |
| -------------------------------------------------------- | --------------------------------------------- |
| **Python (Pandas)**                                      | Limpeza, tradução e preparação dos dados      |
| **Excel**                                                | Análise e visualização dos dados              |
| **Power Pivot**                                          | Modelagem relacional e criação de medidas DAX |
| **Extensões do Excel (Power Query / Tabelas Dinâmicas)** | Carga, exploração e dashboards dinâmicos      |

---

## 📊 **Principais Descobertas**

Durante a análise, foi identificado que o **dispositivo “Chip Móvel”** é o **principal gerador de churn** da empresa.

* Foram **301 chips vendidos** e **91 cancelamentos**, representando **~30% de churn**.
* Apesar de ser o produto mais vendido, ele é o que **menos gera receita**, correspondendo a **menos de 10% da rentabilidade total**.
* Os principais motivos associados ao cancelamento estão ligados a:

  * Tarifas de chamadas altas (54 casos)
  * Melhores ofertas de concorrentes (52 casos)
  * Rede ruim (45 casos)

Esses problemas aparecem com alta frequência entre os usuários de **chips móveis**, reforçando o impacto negativo desse produto na taxa de cancelamento.

---

## 🧾 **Resumo Final**

> A análise permitiu identificar o produto crítico e os principais fatores que impulsionam o churn, possibilitando decisões mais assertivas para reduzir cancelamentos e aumentar a retenção de clientes.

