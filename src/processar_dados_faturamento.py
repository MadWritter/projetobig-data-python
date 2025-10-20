import pandas as pd
import mysql.connector
from time import sleep

def processar_dados_faturamento(conn):
    cursor = conn.cursor()
    # Ler Excel
    excel_path = "dados/venda-itens-faturamento.xlsx"
    df_excel = pd.read_excel(excel_path)

    # Selecionar apenas as colunas relevantes e renomear
    df_excel_sql = df_excel[[
        'Pedido', 'Nome', 'Fantasia', 'Data', 'Descrição', 'SubCategoria',
        'Segmento', 'Natureza', 'Faturado', 'Valor Unitario', 'Valor Total',
        'ValorCorte', 'ValorLiquido', 'Tipo Pg', 'Roteiro', 'Situação'
    ]].rename(columns={
        'Pedido': 'pedido',
        'Nome': 'nome',
        'Fantasia': 'fantasia',
        'Data': 'data',
        'Descrição': 'descricao',
        'SubCategoria': 'sub_categoria',
        'Segmento': 'segmento',
        'Natureza': 'natureza',
        'Faturado': 'faturado',
        'Valor Unitario': 'valor_unitario',
        'Valor Total': 'valor_total',
        'ValorCorte': 'valor_corte',
        'ValorLiquido': 'valor_liquido',
        'Tipo Pg': 'tipo_pg',
        'Roteiro': 'roteiro',
        'Situação': 'situacao'
    })

    # Inserir dados do Excel
    for _, row in df_excel_sql.iterrows():
        cursor.execute("""
            INSERT INTO venda_itens_faturamento (
                pedido, nome, fantasia, data, descricao, sub_categoria, segmento, natureza,
                faturado, valor_unitario, valor_total, valor_corte, valor_liquido,
                tipo_pg, roteiro, situacao
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                nome=VALUES(nome), fantasia=VALUES(fantasia), data=VALUES(data),
                descricao=VALUES(descricao), sub_categoria=VALUES(sub_categoria),
                segmento=VALUES(segmento), natureza=VALUES(natureza),
                faturado=VALUES(faturado), valor_unitario=VALUES(valor_unitario),
                valor_total=VALUES(valor_total), valor_corte=VALUES(valor_corte),
                valor_liquido=VALUES(valor_liquido), tipo_pg=VALUES(tipo_pg),
                roteiro=VALUES(roteiro), situacao=VALUES(situacao)
        """, (
            int(row['pedido']),
            row['nome'],
            row['fantasia'],
            pd.to_datetime(row['data']).date(),
            row['descricao'],
            row['sub_categoria'],
            row['segmento'],
            row['natureza'],
            int(row['faturado']),
            float(row['valor_unitario']),
            float(row['valor_total']),
            float(row['valor_corte']),
            float(row['valor_liquido']),
            row['tipo_pg'],
            row['roteiro'],
            row['situacao']
        ))

    # Commit
    conn.commit()
    cursor.close()
    print("Dados do Excel inseridos com sucesso!")
