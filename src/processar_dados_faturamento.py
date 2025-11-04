import pandas as pd
from time import sleep

def processar_dados_faturamento():
    # Caminho do arquivo Excel
    excel_path = "dados/venda-itens-faturamento.xlsx"

    # Ler Excel
    df_excel = pd.read_excel(excel_path)

    # Selecionar apenas as colunas relevantes e renomear
    df_excel_csv = df_excel[[
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

    # Converter tipos de dados, se necessário
    df_excel_csv['pedido'] = df_excel_csv['pedido'].astype(int)
    df_excel_csv['faturado'] = df_excel_csv['faturado'].astype(int)
    df_excel_csv['data'] = pd.to_datetime(df_excel_csv['data']).dt.date

    for col in ['valor_unitario', 'valor_total', 'valor_corte', 'valor_liquido']:
        df_excel_csv[col] = df_excel_csv[col].astype(float)

    # Caminho do CSV de saída
    csv_path = "dados/venda-itens-faturamento-processado.csv"

    # Exportar para CSV
    df_excel_csv.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')

    print(f"Arquivo CSV gerado com sucesso em: {csv_path}")
