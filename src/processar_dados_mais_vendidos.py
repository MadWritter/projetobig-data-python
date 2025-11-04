import pandas as pd
from time import sleep

def processar_dados_mais_vendidos():
    # Caminho do arquivo Excel
    excel_path = "dados/produtos-mais-vendidos.xlsx"

    # Ler Excel
    df_excel = pd.read_excel(excel_path)

    # Selecionar apenas as colunas relevantes e renomear
    df_excel_csv = df_excel[[
        'Venda', 'Produto', 'Quantidade', 'P. Bruto', 'P. Bruto Total'
    ]].rename(columns={
        'Venda': 'venda',
        'Produto': 'produto',
        'Quantidade': 'quantidade',
        'P. Bruto': 'prod_bruto',
        'P. Bruto Total': 'prod_bruto_total'
    })

    # Converter tipos de dados para manter consistência
    df_excel_csv['venda'] = df_excel_csv['venda'].astype(int)
    df_excel_csv['quantidade'] = df_excel_csv['quantidade'].astype(int)
    df_excel_csv['prod_bruto'] = df_excel_csv['prod_bruto'].astype(float)
    df_excel_csv['prod_bruto_total'] = df_excel_csv['prod_bruto_total'].astype(float)

    # Caminho do CSV de saída
    csv_path = "dados/produtos-mais-vendidos-processado.csv"

    # Exportar para CSV
    df_excel_csv.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')

    print(f"Arquivo CSV gerado com sucesso em: {csv_path}")
