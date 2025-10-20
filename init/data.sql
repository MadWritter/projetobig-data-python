CREATE DATABASE IF NOT EXISTS banco_pandas;
USE banco_pandas;

CREATE TABLE IF NOT EXISTS venda_itens_faturamento (
    pedido BIGINT NOT NULL UNIQUE,
    nome VARCHAR(150) NOT NULL,
    fantasia VARCHAR(150) NOT NULL,
    data DATE NOT NULL,
    descricao VARCHAR(150) NOT NULL,
    sub_categoria VARCHAR(50) NOT NULL,
    segmento VARCHAR(50) NOT NULL,
    natureza VARCHAR(50) NOT NULL,
    faturado INT NOT NULL,
    valor_unitario DECIMAL(10,2) NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    valor_corte DECIMAL(10,2) NOT NULL,
    valor_liquido DECIMAL(10,2) NOT NULL,
    tipo_pg VARCHAR(50) NOT NULL,
    roteiro VARCHAR(50) NOT NULL,
    situacao VARCHAR(50) NOT NULL,
    PRIMARY KEY (pedido)
);

CREATE TABLE IF NOT EXISTS produtos_mais_vendidos(
    id BIGINT NOT NULL AUTO_INCREMENT,
    venda INT NOT NULL,
    produto VARCHAR(200) NOT NULL,
    quantidade INT NOT NULL,
    prod_bruto DECIMAL(10,3) NOT NULL,
    prod_bruto_total DECIMAL(10, 3) NOT NULL,
    PRIMARY KEY (id)
);
