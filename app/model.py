import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

def connect_db(dbname=None):
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_tables():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        date_birth DATE NOT NULL,
        cpf VARCHAR(11) NOT NULL UNIQUE,
        address VARCHAR(255) NOT NULL,
        phone VARCHAR(15),
        email VARCHAR(100)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS course (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        duration INT NOT NULL, -- Duração em horas
        type VARCHAR(50) CHECK (type IN ('Dança', 'Artes Marciais', 'Cursinho Pre Vestibular')) NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teacher_registration (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        speciality VARCHAR(100),
        phone VARCHAR(15),
        email VARCHAR(100)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS class (
        id SERIAL PRIMARY KEY,
        id_course INT REFERENCES course(id),
        id_Prof INT REFERENCES teacher_registration(id),
        name VARCHAR(100) NOT NULL,
        schedule TIME NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS registration (
        id SERIAL PRIMARY KEY,
        id_student INT REFERENCES student(id),
        id_course INT REFERENCES course(id),
        data_birth DATE NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS discipline (
        id SERIAL PRIMARY KEY,
        id_course INT REFERENCES course(id),
        date DATE NOT NULL,
        begin TIME NOT NULL,
        finish TIME NOT NULL,
        local VARCHAR(100) NOT NULL
    );
    ''')
    
    conn.commit()
    conn.close()

def add_student(name, date_birth, cpf, address, phone, email):
    try:
        conn = connect_db()
        if conn is None:
            return "Erro ao conectar ao banco de dados"
        
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO student (name, date_birth, cpf, address, phone, email)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''', (name, date_birth, cpf, address, phone, email))
        
        conn.commit()
        conn.close()
        return "Aluno adicionado com sucesso"
    except Exception as e:
        return f"Erro ao adicionar aluno: {e}"

if __name__ == "__main__":
    create_tables()

def add_teacher(name, speciality, phone, email):
    try:
        conn = connect_db()
        if conn is None:
            return "Erro ao conectar ao banco de dados"
        
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO teacher_registration (name, speciality, phone, email)
        VALUES (%s, %s, %s, %s)
        ''', (name, speciality, phone, email))
        
        conn.commit()
        conn.close()
        return "Professor adicionado com sucesso"
    except Exception as e:
        return f"Erro ao adicionar professor: {e}"

def add_course(name, description, duration, type):
    try:
        conn = connect_db()
        if conn is None:
            return "Erro ao conectar ao banco de dados"
        
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO course (name, description, duration, type)
        VALUES (%s, %s, %s, %s)
        ''', (name, description, duration, type))
        
        conn.commit()
        conn.close()
        return "Curso adicionado com sucesso"
    except Exception as e:
        return f"Erro ao adicionar curso: {e}"

def add_class(id_course, id_prof, name, schedule):
    try:
        conn = connect_db()
        if conn is None:
            return "Erro ao conectar ao banco de dados"
        
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO class (id_course, id_prof, name, schedule)
        VALUES (%s, %s, %s, %s)
        ''', (id_course, id_prof, name, schedule))
        
        conn.commit()
        conn.close()
        return "Turma adicionada com sucesso"
    except Exception as e:
        return f"Erro ao adicionar turma: {e}"

def add_discipline(id_course, date, begin, finish, local):
    try:
        conn = connect_db()
        if conn is None:
            return "Erro ao conectar ao banco de dados"
        
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO discipline (id_course, date, begin, finish, local)
        VALUES (%s, %s, %s, %s, %s)
        ''', (id_course, date, begin, finish, local))
        
        conn.commit()
        conn.close()
        return "Disciplina adicionada com sucesso"
    except Exception as e:
        return f"Erro ao adicionar disciplina: {e}"
