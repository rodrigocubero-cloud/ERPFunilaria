-- Modelo de dados inicial (rascunho)

CREATE TABLE clientes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(200) NOT NULL,
  documento VARCHAR(30),
  telefone VARCHAR(30),
  email VARCHAR(120),
  endereco TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE seguradoras (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(200) NOT NULL,
  contato VARCHAR(200),
  telefone VARCHAR(30),
  email VARCHAR(120)
);

CREATE TABLE veiculos (
  id SERIAL PRIMARY KEY,
  cliente_id INTEGER NOT NULL REFERENCES clientes(id),
  placa VARCHAR(20) NOT NULL,
  modelo VARCHAR(120),
  marca VARCHAR(120),
  ano INTEGER,
  cor VARCHAR(50)
);

CREATE TABLE orcamentos (
  id SERIAL PRIMARY KEY,
  cliente_id INTEGER NOT NULL REFERENCES clientes(id),
  veiculo_id INTEGER NOT NULL REFERENCES veiculos(id),
  seguradora_id INTEGER REFERENCES seguradoras(id),
  status VARCHAR(40) NOT NULL DEFAULT 'rascunho',
  valor_total NUMERIC(12,2) NOT NULL DEFAULT 0,
  validade DATE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE orcamento_itens (
  id SERIAL PRIMARY KEY,
  orcamento_id INTEGER NOT NULL REFERENCES orcamentos(id),
  descricao VARCHAR(255) NOT NULL,
  tipo VARCHAR(40) NOT NULL,
  quantidade NUMERIC(10,2) NOT NULL DEFAULT 1,
  valor_unitario NUMERIC(12,2) NOT NULL DEFAULT 0
);

CREATE TABLE ordens_servico (
  id SERIAL PRIMARY KEY,
  orcamento_id INTEGER REFERENCES orcamentos(id),
  cliente_id INTEGER NOT NULL REFERENCES clientes(id),
  veiculo_id INTEGER NOT NULL REFERENCES veiculos(id),
  status VARCHAR(40) NOT NULL DEFAULT 'aberta',
  previsao_entrega DATE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE os_etapas (
  id SERIAL PRIMARY KEY,
  ordem_servico_id INTEGER NOT NULL REFERENCES ordens_servico(id),
  etapa VARCHAR(80) NOT NULL,
  responsavel VARCHAR(120),
  inicio TIMESTAMP,
  fim TIMESTAMP,
  observacoes TEXT
);

CREATE TABLE estoque_itens (
  id SERIAL PRIMARY KEY,
  sku VARCHAR(60) NOT NULL,
  descricao VARCHAR(255) NOT NULL,
  categoria VARCHAR(80),
  unidade VARCHAR(20),
  estoque_atual NUMERIC(12,2) NOT NULL DEFAULT 0,
  estoque_minimo NUMERIC(12,2) NOT NULL DEFAULT 0
);

CREATE TABLE movimentacoes_estoque (
  id SERIAL PRIMARY KEY,
  item_id INTEGER NOT NULL REFERENCES estoque_itens(id),
  ordem_servico_id INTEGER REFERENCES ordens_servico(id),
  tipo VARCHAR(20) NOT NULL,
  quantidade NUMERIC(12,2) NOT NULL,
  data_movimento TIMESTAMP NOT NULL DEFAULT NOW(),
  observacoes TEXT
);

CREATE TABLE contas (
  id SERIAL PRIMARY KEY,
  tipo VARCHAR(20) NOT NULL,
  descricao VARCHAR(255) NOT NULL,
  valor NUMERIC(12,2) NOT NULL,
  vencimento DATE NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'pendente',
  ordem_servico_id INTEGER REFERENCES ordens_servico(id)
);
