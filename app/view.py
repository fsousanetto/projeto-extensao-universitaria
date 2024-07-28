import tkinter as tk
from tkinter import ttk, messagebox

class AppView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Sistema de Gerenciamento de Cursos")
        self.create_widgets()
        
    def create_widgets(self):
        notebook = ttk.Notebook(self.root)
        
        aluno_tab = ttk.Frame(notebook)
        curso_tab = ttk.Frame(notebook)
        professor_tab = ttk.Frame(notebook)
        aula_tab = ttk.Frame(notebook)
        turma_tab = ttk.Frame(notebook)
        
        notebook.add(aluno_tab, text="Alunos")
        notebook.add(curso_tab, text="Cursos")
        notebook.add(professor_tab, text="Professores")
        notebook.add(aula_tab, text="Aulas")
        notebook.add(turma_tab, text="Turmas")
        
        notebook.pack(expand=True, fill='both')
        
        tk.Label(aluno_tab, text="Cadastro de Alunos", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(aluno_tab, text="Adicionar Novo Aluno", command=self.controller.show_add_student).pack(pady=5)
        tk.Button(aluno_tab, text="Atualizar Dados de Aluno").pack(pady=5)
        tk.Button(aluno_tab, text="Excluir Aluno").pack(pady=5)
        
        tk.Label(curso_tab, text="Gerenciamento de Cursos", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(curso_tab, text="Adicionar Novo Curso", command=self.controller.show_add_course).pack(pady=5)
        tk.Button(curso_tab, text="Atualizar Dados de Curso").pack(pady=5)
        tk.Button(curso_tab, text="Excluir Curso").pack(pady=5)
        
        tk.Label(professor_tab, text="Cadastro de Professores", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(professor_tab, text="Adicionar Novo Professor", command=self.controller.show_add_teacher).pack(pady=5)
        tk.Button(professor_tab, text="Atualizar Dados de Professor").pack(pady=5)
        tk.Button(professor_tab, text="Excluir Professor").pack(pady=5)
        
        tk.Label(aula_tab, text="Gerenciamento de Aulas", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(aula_tab, text="Adicionar Nova Aula", command=self.controller.show_add_discipline).pack(pady=5)
        tk.Button(aula_tab, text="Atualizar Dados de Aula").pack(pady=5)
        tk.Button(aula_tab, text="Excluir Aula").pack(pady=5)
        
        tk.Label(turma_tab, text="Gerenciamento de Turmas", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(turma_tab, text="Criar Nova Turma", command=self.controller.show_add_class).pack(pady=5)
        tk.Button(turma_tab, text="Atualizar Dados de Turma").pack(pady=5)
        tk.Button(turma_tab, text="Excluir Turma").pack(pady=5)
        
    def mainloop(self):
        self.root.mainloop()
        
    def show_add_student_window(self):
        def submit_add():
            name = entry_name.get()
            date_birth = entry_date_birth.get()
            cpf = entry_cpf.get()
            address = entry_address.get()
            phone = entry_phone.get()
            email = entry_email.get()
            result = self.controller.add_student(name, date_birth, cpf, address, phone, email)
            messagebox.showinfo("Resultado", result)
        
        add_window = tk.Toplevel()
        add_window.title("Adicionar Novo Aluno")
        
        tk.Label(add_window, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Data de Nascimento (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
        entry_date_birth = tk.Entry(add_window)
        entry_date_birth.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="CPF:").grid(row=2, column=0, padx=10, pady=5)
        entry_cpf = tk.Entry(add_window)
        entry_cpf.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Endereço:").grid(row=3, column=0, padx=10, pady=5)
        entry_address = tk.Entry(add_window)
        entry_address.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Telefone:").grid(row=4, column=0, padx=10, pady=5)
        entry_phone = tk.Entry(add_window)
        entry_phone.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Email:").grid(row=5, column=0, padx=10, pady=5)
        entry_email = tk.Entry(add_window)
        entry_email.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Button(add_window, text="Adicionar", command=submit_add).grid(row=6, column=0, columnspan=2, pady=10)

    def show_add_course_window(self):
        def submit_add():
            title = entry_title.get()
            description = entry_description.get()
            duration = entry_duration.get()
            type_ = entry_type.get()
            result = self.controller.add_course(title, description, duration, type_)
            messagebox.showinfo("Resultado", result)
        
        add_window = tk.Toplevel()
        add_window.title("Adicionar Novo Curso")
        
        tk.Label(add_window, text="Título:").grid(row=0, column=0, padx=10, pady=5)
        entry_title = tk.Entry(add_window)
        entry_title.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Descrição:").grid(row=1, column=0, padx=10, pady=5)
        entry_description = tk.Entry(add_window)
        entry_description.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Duração:").grid(row=2, column=0, padx=10, pady=5)
        entry_duration = tk.Entry(add_window)
        entry_duration.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Tipo:").grid(row=3, column=0, padx=10, pady=5)
        entry_type = tk.Entry(add_window)
        entry_type.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Button(add_window, text="Adicionar", command=submit_add).grid(row=4, column=0, columnspan=2, pady=10)
    
    def show_add_teacher_window(self):
        def submit_add():
            name = entry_name.get()
            cpf = entry_cpf.get()
            specialty = entry_specialty.get()
            result = self.controller.add_teacher(name, cpf, specialty)
            messagebox.showinfo("Resultado", result)
        
        add_window = tk.Toplevel()
        add_window.title("Adicionar Novo Professor")
        
        tk.Label(add_window, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="CPF:").grid(row=1, column=0, padx=10, pady=5)
        entry_cpf = tk.Entry(add_window)
        entry_cpf.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Especialidade:").grid(row=2, column=0, padx=10, pady=5)
        entry_specialty = tk.Entry(add_window)
        entry_specialty.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(add_window, text="Adicionar", command=submit_add).grid(row=3, column=0, columnspan=2, pady=10)
    
    def show_add_discipline_window(self):
        def submit_add():
            name = entry_name.get()
            description = entry_description.get()
            result = self.controller.add_discipline(name, description)
            messagebox.showinfo("Resultado", result)
        
        add_window = tk.Toplevel()
        add_window.title("Adicionar Nova Aula")
        
        tk.Label(add_window, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Descrição:").grid(row=1, column=0, padx=10, pady=5)
        entry_description = tk.Entry(add_window)
        entry_description.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Button(add_window, text="Adicionar", command=submit_add).grid(row=2, column=0, columnspan=2, pady=10)
    
    def show_add_class_window(self):
        def submit_add():
            name = entry_name.get()
            course = entry_course.get()
            teacher = entry_teacher.get()
            result = self.controller.add_class(name, course, teacher)
            messagebox.showinfo("Resultado", result)
        
        add_window = tk.Toplevel()
        add_window.title("Criar Nova Turma")
        
        tk.Label(add_window, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Curso:").grid(row=1, column=0, padx=10, pady=5)
        entry_course = tk.Entry(add_window)
        entry_course.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Professor:").grid(row=2, column=0, padx=10, pady=5)
        entry_teacher = tk.Entry(add_window)
        entry_teacher.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(add_window, text="Adicionar", command=submit_add).grid(row=3, column=0, columnspan=2, pady=10)
