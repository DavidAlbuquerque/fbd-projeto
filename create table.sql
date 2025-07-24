CREATE TABLE pessoa (
    id SERIAL PRIMARY KEY,
    pnome VARCHAR(50) NOT NULL,
    mnome VARCHAR(50),
    unome VARCHAR(50) NOT NULL,
    sexo VARCHAR(10) NOT NULL CHECK (sexo IN ('Masculino', 'Feminino', 'Outro')),
    data_nascimento DATE NOT NULL CHECK (data_nascimento <= CURRENT_DATE),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE crianca_adolescente (
    id INTEGER PRIMARY KEY REFERENCES pessoa(id),
    numero_prontuario VARCHAR(20) UNIQUE NOT NULL,
    situacao_escolar VARCHAR(20) NOT NULL CHECK (situacao_escolar IN ('Matriculado', 'Evasao', 'Concluido')),
    logradouro VARCHAR(100),
    numero VARCHAR(10),
    bairro VARCHAR(50),
    complemento VARCHAR(50),
    cidade VARCHAR(50),
    responsaveis TEXT NOT NULL
);

CREATE TABLE profissional (
    id INTEGER PRIMARY KEY REFERENCES pessoa(id),
    cpf VARCHAR(14) UNIQUE NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    registro VARCHAR(30)
);

CREATE TABLE avaliacao_risco_social (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL CHECK (data <= CURRENT_DATE),
    instrumento_aplicado TEXT NOT NULL,
    pontuacao INTEGER NOT NULL CHECK (pontuacao >= 0),
    nivel VARCHAR(10) NOT NULL CHECK (nivel IN ('Baixo', 'Moderado', 'Alto')),
    fatores_risco TEXT,
    id_crianca INTEGER NOT NULL REFERENCES crianca_adolescente(id),
    id_profissional INTEGER NOT NULL REFERENCES profissional(id)
);
