INSERT INTO pessoa (pnome, mnome, unome, sexo, data_nascimento, telefone, email) VALUES
('Ana', 'Clara', 'Silva', 'Feminino', '2010-05-12', '85988880001', 'ana.silva@example.com'),
('João', 'Pedro', 'Oliveira', 'Masculino', '2009-09-25', '85988880002', 'joao.oliveira@example.com'),
('Maria', NULL, 'Souza', 'Feminino', '2008-11-03', '85988880003', 'maria.souza@example.com'),
('Lucas', 'Henrique', 'Costa', 'Masculino', '2011-03-18', '85988880004', 'lucas.costa@example.com'),
('Beatriz', 'Fernanda', 'Almeida', 'Feminino', '2012-07-21', '85988880005', 'beatriz.almeida@example.com'),

('Paulo', 'Roberto', 'Lima', 'Masculino', '1980-02-10', '85988880006', 'paulo.lima@example.com'),
('Juliana', NULL, 'Menezes', 'Feminino', '1985-06-28', '85988880007', 'juliana.menezes@example.com'),
('Rafael', 'Augusto', 'Pereira', 'Masculino', '1990-12-15', '85988880008', 'rafael.pereira@example.com'),
('Camila', NULL, 'Nascimento', 'Feminino', '1987-04-03', '85988880009', 'camila.nascimento@example.com'),
('Renato', 'Luiz', 'Martins', 'Masculino', '1978-10-01', '85988880010', 'renato.martins@example.com');

INSERT INTO pessoa (pnome, mnome, unome, sexo, data_nascimento, telefone, email) VALUES
('Bruno', NULL, 'Macedo', 'Masculino', '2007-01-10', '85988880011', 'bruno.macedo@example.com'),
('Larissa', 'Santos', 'Freitas', 'Feminino', '2010-08-14', '85988880012', 'larissa.freitas@example.com'),
('Tiago', 'Antônio', 'Barros', 'Masculino', '2009-06-20', '85988880013', 'tiago.barros@example.com'),
('Carla', 'Regina', 'Monteiro', 'Feminino', '2008-12-01', '85988880014', 'carla.monteiro@example.com'),
('Igor', NULL, 'Ferreira', 'Masculino', '2011-04-30', '85988880015', 'igor.ferreira@example.com'),

('Elaine', 'Cristina', 'Soares', 'Feminino', '1984-03-12', '85988880016', 'elaine.soares@example.com'),
('Sandro', 'Luis', 'Ribeiro', 'Masculino', '1979-09-05', '85988880017', 'sandro.ribeiro@example.com'),
('Marcela', NULL, 'Gonçalves', 'Feminino', '1986-11-27', '85988880018', 'marcela.goncalves@example.com'),
('Carlos', 'Eduardo', 'Moreira', 'Masculino', '1983-05-18', '85988880019', 'carlos.moreira@example.com'),
('Vanessa', 'Lucia', 'Lopes', 'Feminino', '1991-07-08', '85988880020', 'vanessa.lopes@example.com');


INSERT INTO crianca_adolescente (id, numero_prontuario, situacao_escolar, logradouro, numero, bairro, complemento, cidade, responsaveis) VALUES
(1, 'PRT001', 'Matriculado', 'Rua das Flores', '123', 'Centro', NULL, 'Fortaleza', 'Maria da Silva'),
(2, 'PRT002', 'Evasao', 'Av. Brasil', '456', 'Montese', 'Ap 301', 'Fortaleza', 'Carlos Oliveira'),
(3, 'PRT003', 'Matriculado', 'Rua A', '789', 'Benfica', NULL, 'Fortaleza', 'Joana Souza'),
(4, 'PRT004', 'Concluido', 'Rua B', '101', 'Aldeota', NULL, 'Fortaleza', 'Pedro Costa'),
(5, 'PRT005', 'Matriculado', 'Av. Santos Dumont', '2020', 'Papicu', 'Bloco C', 'Fortaleza', 'Fernanda Almeida'),
(11, 'PRT006', 'Matriculado', 'Rua São Paulo', '22', 'Fátima', NULL, 'Fortaleza', 'João Macedo'),
(12, 'PRT007', 'Evasao', 'Rua Ceará', '88', 'Messejana', 'Casa 2', 'Fortaleza', 'Roberta Freitas'),
(13, 'PRT008', 'Matriculado', 'Rua Goiás', '45', 'Parquelândia', NULL, 'Fortaleza', 'Luís Barros'),
(14, 'PRT009', 'Concluido', 'Av. Beira Mar', '502', 'Meireles', NULL, 'Fortaleza', 'Márcia Monteiro'),
(15, 'PRT010', 'Matriculado', 'Rua Amazonas', '10', 'Centro', 'Ap 101', 'Fortaleza', 'Cláudio Ferreira');

INSERT INTO profissional (id, cpf, cargo, registro) VALUES
(6, '123.456.789-00', 'Psicólogo', 'CRP-001'),
(7, '987.654.321-11', 'Assistente Social', 'AS-045'),
(8, '111.222.333-44', 'Psicólogo', 'CRP-002'),
(9, '555.666.777-88', 'Pedagogo', 'PED-009'),
(10, '000.999.888-77', 'Assistente Social', 'AS-067'),
(16, '321.654.987-00', 'Psicólogo', 'CRP-010'),
(17, '741.852.963-11', 'Assistente Social', 'AS-099'),
(18, '369.258.147-22', 'Psicólogo', 'CRP-011'),
(19, '159.753.486-33', 'Pedagogo', 'PED-014'),
(20, '951.357.258-44', 'Assistente Social', 'AS-123');

INSERT INTO avaliacao_risco_social (data, instrumento_aplicado, pontuacao, nivel, fatores_risco, id_crianca, id_profissional) VALUES
('2024-06-01', 'Escala A', 12, 'Moderado', 'Falta de renda, ausência parental', 1, 6),
('2024-06-05', 'Escala B', 8, 'Baixo', 'Rendimento escolar baixo', 2, 7),
('2024-06-10', 'Escala A', 16, 'Alto', 'Violência doméstica, evasão escolar', 3, 8),
('2024-06-15', 'Escala C', 7, 'Baixo', 'Problemas de moradia', 4, 9),
('2024-06-20', 'Escala B', 11, 'Moderado', 'Conflitos familiares, baixa autoestima', 5, 10),
('2024-06-25', 'Escala A', 17, 'Alto', 'Desnutrição, negligência', 1, 6),
('2024-07-01', 'Escala B', 6, 'Baixo', 'Falta de acompanhamento escolar', 2, 7),
('2024-07-05', 'Escala C', 14, 'Moderado', 'Moradia precária, trabalho infantil', 3, 8),
('2024-07-10', 'Escala A', 19, 'Alto', 'Histórico de abuso, abandono', 4, 9),
('2024-07-15', 'Escala C', 10, 'Moderado', 'Risco de evasão escolar, depressão', 5, 10);


INSERT INTO Agenda_Atendimento (data, hora, status, frequencia, tipo, id_profissional, id_crianca_adolescente) VALUES
('2024-07-01', '09:00:00', 'Agendado', 'Semanal', 'Psicólogo', 6, 1),
('2024-07-02', '10:30:00', 'Concluido', 'Mensal', 'Assistente Social', 7, 2),
('2024-07-03', '14:00:00', 'Cancelado', 'Quizenal', 'Psicólogo', 8, 3),
('2024-07-04', '08:00:00', 'Agendado', 'Semanal', 'Pedagogo', 9, 4),
('2024-07-05', '15:00:00', 'Agendado', 'Mensal', 'Assistente Social', 10, 5),
('2024-07-06', '09:30:00', 'Concluido', 'Semanal', 'Psicólogo', 16, 11),
('2024-07-07', '13:00:00', 'Agendado', 'Quizenal', 'Assistente Social', 17, 12),
('2024-07-08', '11:15:00', 'Agendado', 'Bimestral', 'Psicólogo', 18, 13),
('2024-07-09', '10:00:00', 'Cancelado', 'Semanal', 'Pedagogo', 19, 14),
('2024-07-10', '16:30:00', 'Agendado', 'Mensal', 'Assistente Social', 20, 15);