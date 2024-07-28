CREATE DATABASE GerenciamentoCourses;

-- Tabela aluno
CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_birth DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100)
);

-- Tabela curso
CREATE TABLE course (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration INT NOT NULL, -- Duração em horas
    type VARCHAR(50) CHECK (type IN ('Dança', 'Artes Marciais','Curso de Capacitação' , 'Cursinho Pre Vestibular')) NOT NULL
);

-- Tabela cadastro de professor
CREATE TABLE teacher_registration (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    speciality VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100)
);

-- Tabela turma
CREATE TABLE class (
    id SERIAL PRIMARY KEY,
    id_course INT REFERENCES course(id),
    id_Prof INT REFERENCES teacher_registration(id),
    name VARCHAR(100) NOT NULL,
    schedule TIME NOT NULL
);

-- Tabela matrícula
CREATE TABLE registration (
    id SERIAL PRIMARY KEY,
    id_student INT REFERENCES student(id),
    id_course INT REFERENCES course(id),
    data_birth DATE NOT NULL
);

-- Tabela aula
CREATE TABLE discipline (
    id SERIAL PRIMARY KEY,
    id_course INT REFERENCES course(id),
    date DATE NOT NULL,
    begin TIME NOT NULL,
    finish TIME NOT NULL,
    local VARCHAR(100) NOT NULL
);
