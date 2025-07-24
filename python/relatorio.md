# Relatório FBD

**Trabalho de Fundamentos de Banco de Dados**  
**Sistema de Acompanhamento de Crianças e Adolescentes em Risco Social**

**Equipe:**
- Alícia Maria Gualberto Lima — 514088 — Engenharia da Computação
- David Gabriel de Albuquerque Alves — 509828 — Engenharia da Computação
- David Silva Fernandes de Oliveira — 539402 — Engenharia da Computação  
**Professora:** Lívia Almada Cruz

---

## 1. Introdução

O Sistema de Acompanhamento de Crianças e Adolescentes em Risco Social tem a proposta de cuidar e organizar as informações de crianças e adolescentes que vivem em situações de vulnerabilidade. Seu principal objetivo é centralizar, organizar e disponibilizar dados muito importantes para o acompanhamento de crianças e adolescentes, facilitando a tomada de decisão por parte de profissionais das áreas de assistência social, psicologia, pedagogia e saúde em relação à situação de vulnerabilidade.

A plataforma permite o registro detalhado e a consulta bem definida de informações como histórico escolar, sessões de atendimento psicológico, relatórios de visitas domiciliares, avaliações de risco social e participação em programas e políticas públicas. Ao reunir esses dados de forma organizada, o sistema ajuda a formar uma visão mais completa sobre a vida escolar, emocional e social de cada criança e adolescente acompanhado.

---

## 2. Descrição dos Requisitos Funcionais

### REQ 001 — Cadastro de crianças/adolescentes
**Descrição:** Inserir, editar, remover e listar crianças ou adolescentes acompanhados.  
**Dados:** ID, nome completo, data de nascimento, sexo, nome do(s) responsável(is), endereço, telefone/e-mail, situação escolar (Matriculado, Evasão, Concluído), nº de prontuário.  
**Restrições:** Nº de prontuário único; data de nascimento não pode ser futura; nome e responsáveis são obrigatórios.

### REQ 002 — Cadastro de Profissionais
**Descrição:** Cadastrar e gerenciar psicólogos, assistentes sociais, pedagogos e demais profissionais.  
**Dados:** ID, nome completo, CPF, cargo/função, instituição de vínculo, registro profissional, e-mail/telefone.  
**Restrições:** CPF único e válido; apenas administradores podem cadastrar.

### REQ 003 — Agenda de Atendimentos
**Descrição:** Agendar, reprogramar, cancelar e listar sessões psicológicas, visitas domiciliares ou reuniões escolares.  
**Dados:** ID, nome da criança/adolescente, profissional, tipo, data/hora, endereço, status.  
**Restrições:** Não pode haver sobreposição de horário para o mesmo profissional.

### REQ 004 — Histórico escolar
**Descrição:** Registrar e consultar registros de histórico escolar.  
**Dados:** Nome, escola, ano letivo, bimestre, série/ano, disciplinas, nota e frequência.  
**Restrições:** Ano letivo não pode ser futuro; notas entre 0 e 10; frequência não pode ultrapassar dias letivos.

### REQ 005 — Acompanhamento psicológico
**Descrição:** Registrar e consultar sessões de atendimento psicológico.  
**Dados:** ID, data/hora, profissional, criança/adolescente, endereço, observações, encaminhamentos.  
**Restrições:** Profissional deve existir; sessão vinculada a uma única criança/adolescente.

### REQ 006 — Visitas Domiciliares
**Descrição:** Inserir relatórios de visitas domiciliares.  
**Dados:** ID, criança/adolescente, profissional, data, endereço, descrição, observações.  
**Restrições:** Data não futura; edição apenas pelo autor ou administrador.

### REQ 007 — Programas Sociais
**Descrição:** Permite o cadastro de programas sociais.  
**Dados:** ID, nome, órgão responsável, público-alvo, critérios, regras, descrição, benefícios.  
**Restrições:** Nome único; órgão responsável deve existir.

### REQ 008 — Alertas e Notificações
**Descrição:** Enviar alertas automáticos por e-mail/telefone.  
**Dados:** Motivo, data/hora, email/telefone.  
**Restrições:** Apenas usuários que optarem por alertas; email/telefone válido; sem alertas duplicados.

### REQ 009 — Cadastro de Administradores
**Descrição:** Cadastro de administrador para validação, gerenciamento e supervisão.  
**Dados:** ID, nome, e-mail, senha.  
**Restrições:** Apenas administradores cadastrados podem criar outros; e-mail único e senha segura.

### REQ 010 — Relatórios Gerenciais
**Descrição:** Gerar relatórios sobre usuários, atendimentos, programas, indicadores.  
**Dados:** ID, filtros, data, descrição.  
**Restrições:** Apenas administradores e profissionais autorizados.

### REQ 011 — Encaminhamentos Externos
**Descrição:** Registrar encaminhamentos para serviços externos.  
**Dados:** ID, nome, profissional, instituição, data, motivo, status, retorno previsto.  
**Restrições:** Data válida; instituição cadastrada; apenas profissionais autorizados.

### REQ 012 — Avaliação de Risco Social
**Descrição:** Registrar avaliações formais e calcular nível de vulnerabilidade.  
**Dados:** ID, nome, profissional, data, instrumento, pontuação, nível, fatores.  
**Restrições:** Pontuação válida conforme instrumento; apenas profissionais autorizados.

---

## 3. Descrição do Modelo ER/EER

### 3.1 Superentidade Pessoa e Especializações
Entidade genérica `Pessoa` com:
- id
- nome (pnome, mnome, unome)
- sexo
- data_nascimento
- contato (telefone, email)

Especializações:
- `Criança/Adolescente`: numero_prontuario, situacao_escolar, responsaveis, endereco.
- `Profissional`: cpf, cargo, registro.

### 3.2 Administrador
- id
- nome
- email
- senha_hash

### 3.3 Agenda de Atendimentos e Especializações
Entidade: `Agenda de Atendimento`
- id, data, hora, tipo, status, frequencia

Relacionamentos:
- `Preenche`: Profissional (0,N) → Agendamento (1,1)
- `Sobre`: Criança/Adolescente (0,N) → Agendamento (1,1)

Especializações:
- `Sessão`: encaminhamentos
- `Visita`: descricao, higiene, estrutura, seguranca

### 3.4 Encaminhamentos Externos
- id, data, motivo, status, instituicao_destino, retorno_previsto

Relacionamentos:
- `Encaminha`: Profissional (1,N) → Encaminhamento (1,1)
- Criança/Adolescente (0,N) → Encaminhamento (1,1)

### 3.5 Avaliação de Risco Social
- id, data, instrumento_aplicado, pontuacao, nivel, fatores_risco

Relacionamentos:
- `Avalia`: Profissional (1,N) → Avaliação (1,1)
- Criança/Adolescente (0,N) → Avaliação (1,1)

### 3.6 Relatório Gerencial
- id, descricao, data_geracao, periodo_inicio, periodo_fim

Relacionamentos:
- `Gera`: Profissional (1,N) → Relatório (1,1)
- `ÉFocoDe` com:
  - Criança/Adolescente
  - Histórico Escolar
  - Programas Sociais

### 3.7 Histórico Escolar
Entidade fraca dependente de Criança/Adolescente.  
Atributos:
- escola, ano_letivo, serie_ano, bimestre, disciplinas, notas, frequencia

### 3.8 Programas Sociais
- id, nome, orgao_responsavel, descricao, beneficios, criterios, regras, publico_alvo

Relacionamentos:
- `Participa`: Criança (0,N) ↔ Programa (0,N)
- `ÉFocoDe`: Relatório (1,1) ↔ Programa (0,N)

### 3.9 Alertas e Notificações
Relacionamento recursivo `Recebe Alerta`:
- motivo, data, hora
- remetente (Pessoa)
- destinatário (Pessoa)

---

## 4. Diagrama ER/EER
Disponível em:  
[Diagrama ER/EER no Canva](https://www.canva.com/design/DAGpsHw52u0/hoFxwVDA01xGocQxci6I0w/edit)

---

## 5. Descrição do Esquema Relacional
Modelo baseado em `Pessoa`, especializado em `Administrador`, `Profissional`, `Criança/Adolescente`, com uso de tabelas auxiliares para atributos multivalorados.

---

## 6. Diagrama do Esquema Relacional
Disponível em:  
[Diagrama do Esquema Relacional no Canva](https://www.canva.com/design/DAGqT5N8uBQ/RAPQduwF53ZR1WM7mkP_Ew/edit)

---

## 7. Telas
- Avaliação de Risco Social
- Crianças/Adolescentes
- Agenda de Atendimentos

---

## 8. Tarefas realizadas por cada membro da equipe
(Ver tabela de atividades descrita no relatório)

---

## 9. Conclusão

O trabalho apresentou a modelagem conceitual e relacional de um sistema de acompanhamento de crianças e adolescentes em situação de risco social, utilizando superentidades, especializações, entidades fracas, e relacionamentos recursivos. A estrutura proposta assegura integridade, escalabilidade, e integração com outras plataformas, promovendo uma base robusta para operações e análises.

---

## 10. Apresentação
Disponível em:  
[Apresentação Projeto FBD (Parte 1)](https://drive.google.com/drive/folders/1T_sR-mcmZcy4cZItG4CJKBP6lFkgHcqI?usp=drive_link)
