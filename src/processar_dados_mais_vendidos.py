import pandas as pd
import mysql.connector
from time import sleep

def processar_dados_mais_vendidos(conn):
    cursor = conn.cursor()
    # Ler Excel
    excel_path = "dados/produtos-mais-vendidos.xlsx"
    df_excel = pd.read_excel(excel_path)

    # Selecionar apenas as colunas relevantes e renomear
    df_excel_sql = df_excel[[
        'Venda', 'Produto', 'Quantidade', 'P. Bruto', 'P. Bruto Total'
    ]].rename(columns={
        'Venda': 'venda',
        'Produto': 'produto',
        'Quantidade': 'quantidade',
        'P. Bruto': 'prod_bruto',
        'P. Bruto Total': 'prod_bruto_total'
    })

    # Inserir dados do Excel
    for _, row in df_excel_sql.iterrows():
        cursor.execute("""
            INSERT INTO produtos_mais_vendidos (
                venda, produto, quantidade, prod_bruto, prod_bruto_total
            ) VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                venda=VALUES(venda), produto=VALUES(produto), quantidade=VALUES(quantidade),
                prod_bruto=VALUES(prod_bruto), prod_bruto_total=VALUES(prod_bruto_total)
        """, (
            int(row['venda']),
            row['produto'],
            int(row['quantidade']),
            float(row['prod_bruto']),
            float(row['prod_bruto_total'])
        ))

    # Commit
    conn.commit()
    cursor.close()
    print("Dados do Excel inseridos com sucesso!")
