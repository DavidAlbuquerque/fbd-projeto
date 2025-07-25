-- Script para criar as tabelas do sistema de avaliação de risco social
-- Inclui as tabelas relacionadas: crianca_adolescente, profissional e avaliacao_risco_social

-- Tabela de crianças e adolescentes
CREATE TABLE public.crianca_adolescente
(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    numero_prontuario VARCHAR(20) UNIQUE NOT NULL,
    data_nascimento DATE,
    cpf VARCHAR(14),
    endereco TEXT,
    telefone VARCHAR(20)
);

-- Tabela de profissionais
CREATE TABLE public.profissional
(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    registro_profissional VARCHAR(20),
    cargo VARCHAR(50),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela de avaliações de risco social
CREATE TABLE public.avaliacao_risco_social
(
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    instrumento_aplicado TEXT NOT NULL,
    pontuacao INTEGER NOT NULL,
    nivel VARCHAR(10) NOT NULL,
    fatores_risco TEXT,
    id_crianca INTEGER NOT NULL,
    id_profissional INTEGER NOT NULL,
    FOREIGN KEY (id_crianca) REFERENCES crianca_adolescente(id),
    FOREIGN KEY (id_profissional) REFERENCES profissional(id)
);

-- Comentários das tabelas
COMMENT ON TABLE public.crianca_adolescente IS 'Tabela de crianças e adolescentes';
COMMENT ON TABLE public.profissional IS 'Tabela de profissionais';
COMMENT ON TABLE public.avaliacao_risco_social IS 'Tabela para armazenar avaliações de risco social';

-- Inserir dados de exemplo

-- Inserir crianças/adolescentes de exemplo
INSERT INTO public.crianca_adolescente 
(nome, numero_prontuario, data_nascimento, cpf) 
VALUES 
('João Silva Santos', 'P001', '2010-05-15', '123.456.789-00'),
('Maria Oliveira Costa', 'P002', '2012-08-22', '987.654.321-00'),
('Pedro Souza Lima', 'P003', '2008-12-10', '456.789.123-00');

-- Inserir profissionais de exemplo
INSERT INTO public.profissional 
(nome, cpf, registro_profissional, cargo) 
VALUES 
('Dr. Ana Paula Ribeiro', '111.222.333-44', 'CRP 12345', 'Psicóloga'),
('Assistente Social Carlos Silva', '555.666.777-88', 'CRESS 6789', 'Assistente Social');

-- Inserir avaliações de exemplo
INSERT INTO public.avaliacao_risco_social 
(data, instrumento_aplicado, pontuacao, nivel, fatores_risco, id_crianca, id_profissional) 
VALUES 
('2024-01-15', 'Escala de Avaliação de Risco Familiar', 25, 'Moderado', 'Vulnerabilidade socioeconômica, ausência de rede de apoio', 1, 1),
('2024-01-16', 'Protocolo de Avaliação Social', 15, 'Baixo', 'Família estruturada, renda estável', 2, 1),
('2024-01-17', 'Instrumento de Análise de Contexto', 40, 'Alto', 'Violência doméstica, uso de substâncias', 3, 2); 