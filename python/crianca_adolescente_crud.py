#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Acompanhamento de Crianças e Adolescentes em Risco Social
CRUD para gerenciamento de crianças e adolescentes
"""

import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2 as pg
import sqlalchemy
from sqlalchemy import create_engine
import panel as pn

# Carrega as variáveis do arquivo .env
load_dotenv()

# Lê as variáveis de ambiente
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Cria conexão com psycopg2
con = pg.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)

# Define a string de conexão para o SQLAlchemy
cnx = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
engine = sqlalchemy.create_engine(cnx)

# Inicializa as extensões do Panel
pn.extension()
pn.extension('tabulator')
pn.extension(notifications=True)

# Widgets de entrada para dados pessoais
pnome = pn.widgets.TextInput(
    name="Primeiro Nome *",
    value='',
    placeholder='Digite o primeiro nome',
    disabled=False
)

mnome = pn.widgets.TextInput(
    name="Nome do Meio",
    value='',
    placeholder='Digite o nome do meio (opcional)',
    disabled=False
)

unome = pn.widgets.TextInput(
    name="Sobrenome *",
    value='',
    placeholder='Digite o sobrenome',
    disabled=False
)

sexo = pn.widgets.RadioBoxGroup(
    name='Sexo *', 
    options=['Todos', 'Masculino', 'Feminino'],
    value='Todos'
)

data_nascimento = pn.widgets.DatePicker(
    name='Data de Nascimento *',
    disabled=False
)

telefone = pn.widgets.TextInput(
    name="Telefone",
    value='',
    placeholder='Digite o telefone',
    disabled=False
)

email = pn.widgets.TextInput(
    name="E-mail",
    value='',
    placeholder='Digite o e-mail',
    disabled=False
)

# Widgets específicos para crianças/adolescentes
numero_prontuario = pn.widgets.TextInput(
    name="Número do Prontuário *",
    value='',
    placeholder='Digite o número do prontuário',
    disabled=False
)

situacao_escolar = pn.widgets.RadioBoxGroup(
    name='Situação Escolar *', 
    options=['Todos', 'Matriculado', 'Evasao', 'Concluido'],
    value='Todos'
)

logradouro = pn.widgets.TextInput(
    name="Logradouro *",
    value='',
    placeholder='Digite o logradouro',
    disabled=False
)

numero = pn.widgets.TextInput(
    name="Número *",
    value='',
    placeholder='Digite o número',
    disabled=False
)

bairro = pn.widgets.TextInput(
    name="Bairro *",
    value='',
    placeholder='Digite o bairro',
    disabled=False
)

complemento = pn.widgets.TextInput(
    name="Complemento",
    value='',
    placeholder='Digite o complemento (opcional)',
    disabled=False
)

cidade = pn.widgets.TextInput(
    name="Cidade *",
    value='',
    placeholder='Digite a cidade',
    disabled=False
)

responsaveis = pn.widgets.TextAreaInput(
    name="Responsáveis *",
    value='',
    placeholder='Digite os responsáveis',
    disabled=False,
    height=100
)

# Botões de ação
buttonConsultar = pn.widgets.Button(name='🔍 Consultar', button_type='primary')
buttonInserir = pn.widgets.Button(name='➕ Inserir', button_type='success')
buttonExcluir = pn.widgets.Button(name='🗑️ Excluir', button_type='danger')
buttonAtualizar = pn.widgets.Button(name='✏️ Atualizar', button_type='warning')
buttonLimpar = pn.widgets.Button(name='🧹 Limpar', button_type='default')

# Função para limpar todos os campos do formulário
def limpar_campos(event=None):
    pnome.value = ''
    mnome.value = ''
    unome.value = ''
    sexo.value = 'Todos'  # Volta para "Todos"
    data_nascimento.value = None  # Limpa a data
    telefone.value = ''
    email.value = ''
    numero_prontuario.value = ''
    situacao_escolar.value = 'Todos'  # Volta para "Todos"
    logradouro.value = ''
    numero.value = ''
    bairro.value = ''
    complemento.value = ''
    cidade.value = ''
    responsaveis.value = ''

buttonLimpar.on_click(limpar_campos)

def queryAll():
    """
    Consulta todos os registros de crianças/adolescentes
    """
    query = """
    SELECT 
        p.id,
        p.pnome,
        p.mnome,
        p.unome,
        p.sexo,
        p.data_nascimento,
        p.telefone,
        p.email,
        ca.numero_prontuario,
        ca.situacao_escolar,
        ca.logradouro,
        ca.numero,
        ca.bairro,
        ca.complemento,
        ca.cidade,
        ca.responsaveis
    FROM pessoa p
    INNER JOIN crianca_adolescente ca ON p.id = ca.id
    ORDER BY p.pnome, p.unome;
    """
    df = pd.read_sql_query(query, cnx)
    return pn.widgets.Tabulator(df)

def on_consultar():
    """
    Consulta registros com múltiplos filtros (prontuário, e-mail, nome, etc.)
    """
    try:
        # Monta a query base
        query = """
        SELECT 
            p.id, p.pnome, p.mnome, p.unome, p.sexo, p.data_nascimento,
            p.telefone, p.email, ca.numero_prontuario, ca.situacao_escolar,
            ca.logradouro, ca.numero, ca.bairro, ca.complemento, ca.cidade, ca.responsaveis
        FROM pessoa p
        INNER JOIN crianca_adolescente ca ON p.id = ca.id
        """
        filtros = []
        params = []

        # Adiciona filtros conforme os campos preenchidos
        if numero_prontuario.value_input:
            filtros.append("ca.numero_prontuario = %s")
            params.append(numero_prontuario.value_input)
        if email.value_input:
            filtros.append("p.email = %s")
            params.append(email.value_input)
        if pnome.value_input:
            filtros.append("p.pnome ILIKE %s")
            params.append(f"%{pnome.value_input}%")
        if unome.value_input:
            filtros.append("p.unome ILIKE %s")
            params.append(f"%{unome.value_input}%")
        # Só filtra sexo se não for 'Todos'
        if sexo.value and sexo.value != 'Todos':
            filtros.append("p.sexo = %s")
            params.append(sexo.value)
        if data_nascimento.value:
            filtros.append("p.data_nascimento = %s")
            params.append(str(data_nascimento.value))
        if telefone.value_input:
            filtros.append("p.telefone ILIKE %s")
            params.append(f"%{telefone.value_input}%")
        if email.value_input:
            filtros.append("p.email ILIKE %s")
            params.append(f"%{email.value_input}%")
        if situacao_escolar.value and situacao_escolar.value != 'Todos':
            filtros.append("ca.situacao_escolar = %s")
            params.append(situacao_escolar.value)
        

        # Monta a cláusula WHERE se houver filtros
        if filtros:
            query += " WHERE " + " AND ".join(filtros)
        query += " ORDER BY p.pnome, p.unome;"

        # Executa a consulta
        df = pd.read_sql_query(query, cnx, params=tuple(params))
        table = pn.widgets.Tabulator(df)
        return table
    except Exception as e:
        return pn.pane.Alert(f'❌ Não foi possível consultar: {str(e)}')

def on_inserir():
    """
    Insere um novo registro de criança/adolescente
    """
    
    if sexo.value == 'Todos':
        return pn.pane.Alert('Por favor, selecione Masculino ou Feminino para o campo Sexo ao inserir um registro.', alert_type='warning')
    try:
        cursor = con.cursor()
        
        # Inserir na tabela pessoa primeiro
        cursor.execute("""
            INSERT INTO pessoa(pnome, mnome, unome, sexo, data_nascimento, telefone, email) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) 
            RETURNING id
        """, (
            pnome.value_input, 
            mnome.value_input if mnome.value_input else None,
            unome.value_input, 
            sexo.value, 
            data_nascimento.value, 
            telefone.value_input if telefone.value_input else None,
            email.value_input if email.value_input else None
        ))
        
        pessoa_id = cursor.fetchone()[0]
        
        # Inserir na tabela crianca_adolescente
        cursor.execute("""
            INSERT INTO crianca_adolescente(
                id, numero_prontuario, situacao_escolar, logradouro, numero, 
                bairro, complemento, cidade, responsaveis
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            pessoa_id,
            numero_prontuario.value_input,
            situacao_escolar.value,
            logradouro.value_input if logradouro.value_input else None,
            numero.value_input if numero.value_input else None,
            bairro.value_input if bairro.value_input else None,
            complemento.value_input if complemento.value_input else None,
            cidade.value_input if cidade.value_input else None,
            responsaveis.value_input
        ))
        
        con.commit()
        cursor.close()
        return pn.pane.Alert('✅ Registro inserido com sucesso!')
    except Exception as e:
        con.rollback()
        return pn.pane.Alert(f'❌ Não foi possível inserir: {str(e)}')

def on_atualizar():
    """
    Atualiza um registro existente (atualização parcial: só campos preenchidos são alterados)
    """
    try:
        cursor = con.cursor()
        # Buscar valores atuais do registro
        cursor.execute('''
            SELECT p.pnome, p.mnome, p.unome, p.sexo, p.data_nascimento, p.telefone, p.email,
                   ca.situacao_escolar, ca.logradouro, ca.numero, ca.bairro, ca.complemento, ca.cidade, ca.responsaveis
            FROM pessoa p
            INNER JOIN crianca_adolescente ca ON p.id = ca.id
            WHERE ca.numero_prontuario = %s
        ''', (numero_prontuario.value_input,))
        result = cursor.fetchone()
        if not result:
            cursor.close()
            return pn.pane.Alert('❌ Prontuário não encontrado para atualização.')
        (
            old_pnome, old_mnome, old_unome, old_sexo, old_data_nascimento, old_telefone, old_email,
            old_situacao_escolar, old_logradouro, old_numero, old_bairro, old_complemento, old_cidade, old_responsaveis
        ) = result

        # Usa o valor do campo se preenchido, senão mantém o antigo
        new_pnome = pnome.value_input if pnome.value_input else old_pnome
        new_mnome = mnome.value_input if mnome.value_input else old_mnome
        new_unome = unome.value_input if unome.value_input else old_unome
        new_sexo = sexo.value if sexo.value and sexo.value != 'Todos' else old_sexo
        new_data_nascimento = data_nascimento.value if data_nascimento.value else old_data_nascimento
        new_telefone = telefone.value_input if telefone.value_input else old_telefone
        new_email = email.value_input if email.value_input else old_email
        new_situacao_escolar = situacao_escolar.value if situacao_escolar.value else old_situacao_escolar
        new_logradouro = logradouro.value_input if logradouro.value_input else old_logradouro
        new_numero = numero.value_input if numero.value_input else old_numero
        new_bairro = bairro.value_input if bairro.value_input else old_bairro
        new_complemento = complemento.value_input if complemento.value_input else old_complemento
        new_cidade = cidade.value_input if cidade.value_input else old_cidade
        new_responsaveis = responsaveis.value_input if responsaveis.value_input else old_responsaveis

        # Atualizar dados da pessoa
        cursor.execute('''
            UPDATE pessoa 
            SET pnome = %s, mnome = %s, unome = %s, sexo = %s, 
                data_nascimento = %s, telefone = %s, email = %s
            WHERE id = (SELECT id FROM crianca_adolescente WHERE numero_prontuario = %s)
        ''', (
            new_pnome, new_mnome, new_unome, new_sexo, new_data_nascimento, new_telefone, new_email, numero_prontuario.value_input
        ))

        # Atualizar dados da criança/adolescente
        cursor.execute('''
            UPDATE crianca_adolescente 
            SET situacao_escolar = %s, logradouro = %s, numero = %s, 
                bairro = %s, complemento = %s, cidade = %s, responsaveis = %s
            WHERE numero_prontuario = %s
        ''', (
            new_situacao_escolar, new_logradouro, new_numero, new_bairro, new_complemento, new_cidade, new_responsaveis, numero_prontuario.value_input
        ))

        con.commit()
        cursor.close()
        return pn.pane.Alert('✅ Registro atualizado com sucesso!')
    except Exception as e:
        con.rollback()
        return pn.pane.Alert(f'❌ Não foi possível atualizar: {str(e)}')

def on_excluir():
    """
    Exclui um registro por número do prontuário
    """
    try:
        cursor = con.cursor()
        
        # Excluir da tabela crianca_adolescente primeiro (devido à FK)
        cursor.execute("""
            DELETE FROM crianca_adolescente 
            WHERE numero_prontuario = %s
        """, (numero_prontuario.value_input,))
        
        # A exclusão da pessoa será feita automaticamente se configurada como CASCADE
        # Caso contrário, seria necessário excluir manualmente
        
        con.commit()
        cursor.close()
        return pn.pane.Alert('✅ Registro excluído com sucesso!')
    except Exception as e:
        con.rollback()
        return pn.pane.Alert(f'❌ Não foi possível excluir: {str(e)}')

def table_creator(cons, ins, atu, exc):
    if cons:
        return on_consultar()
    if ins:
        return on_inserir()
    if atu:
        return on_atualizar()
    if exc:
        return on_excluir()

# Cria a ligação interativa
interactive_table = pn.bind(table_creator, buttonConsultar, buttonInserir, buttonAtualizar, buttonExcluir)

# Monta o layout da interface
app = pn.Row(
    pn.Column(
        pn.pane.Markdown('# 👶 Sistema de Crianças e Adolescentes'),
        pn.pane.Markdown('### 📋 Dados Pessoais'),
        pnome, mnome, unome, sexo, data_nascimento, telefone, email,
        pn.pane.Markdown('### 🏠 Dados Específicos'),
        numero_prontuario, situacao_escolar, logradouro, numero, bairro, complemento, cidade, responsaveis,
        pn.pane.Markdown('### ⚡ Ações'),
        pn.Row(buttonConsultar),
        pn.Row(buttonInserir),
        pn.Row(buttonAtualizar),
        pn.Row(buttonExcluir),
        pn.Row(buttonLimpar)
    ),
    pn.Column(
        pn.pane.Markdown('### 📊 Dados Cadastrados'),
        interactive_table
    )
).servable()

if __name__ == "__main__":
    app.show() 