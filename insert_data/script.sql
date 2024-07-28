-- insert student
INSERT INTO student (name, date_birthc, cpf, address, phone, email) VALUES
('João Silva', '2000-01-15', '12345678900', 'Rua A, 123', '91987654321', 'joao.silva@example.com'),
('Maria Oliveira', '1995-06-23', '91765432100', 'Rua B, 456', '91987654322', 'maria.oliveira@example.com');

-- insert course
INSERT INTO course (name, description, duration, type) VALUES
('Dança Clássica', 'Curso de dança clássica para iniciantes.', 40, 'Dança'),
('Karate', 'Curso de Karate para todos os níveis.', 60, 'Artes Marciais'),
('Pré-Vestibular', 'Curso preparatório para vestibular.', 100, 'Cursinho Pre Vestibular');

-- insert teacher
INSERT INTO teacher_registration (name, speciality, phone, email) VALUES
('Carlos Lima', 'Dança Clássica', '91987654330', 'carlos.lima@example.com'),
('Ana Souza', 'Karate', '91987654331', 'ana.souza@example.com');

-- insert class
INSERT INTO class (id_course, id_prof, name, schedule) VALUES
(1, 1, 'Turma 1 - Dança Clássica', '10:00:00'),
(2, 2, 'Turma 1 - Karate', '15:00:00');

-- insert registration
INSERT INTO registration (id_student, id_course, data_birth) VALUES
(1, 1, '2000-01-15'),
(2, 2, '1995-06-23');

-- insert discipline
INSERT INTO discipline (id_course, date, begin, finish, local) VALUES
(1, '2024-08-01', '10:00:00', '12:00:00', 'Salão 1'),
(2, '2024-08-02', '15:00:00', '17:00:00', 'Quadra 2');
