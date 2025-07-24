

CREATE TABLE public.pessoa
(
idp serial,
nome character varying(50),
cpf character varying(12),
sexo character varying(12),
nascimento date,
salario numeric(1000,2),
CONSTRAINT pessoa_pkey PRIMARY KEY (cpf),
CONSTRAINT id_unique UNIQUE (idp)
INCLUDE(idp)
);
