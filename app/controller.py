from model import create_tables, add_student, add_teacher, add_course, add_class, add_discipline
from view import AppView

class AppController:
    def __init__(self):
        self.view = AppView(self)
        create_tables()
    
    def show_add_student(self):
        self.view.show_add_student_window()
    
    def add_student(self, name, date_birth, cpf, address, phone, email):
        return add_student(name, date_birth, cpf, address, phone, email)
    
    def show_add_teacher(self):
        self.view.show_add_teacher_window()
    
    def add_teacher(self, name, speciality, phone, email):
        return add_teacher(name, speciality, phone, email)
    
    def show_add_course(self):
        self.view.show_add_course_window()
    
    def add_course(self, name, description, duration, type):
        return add_course(name, description, duration, type)
    
    def show_add_class(self):
        self.view.show_add_class_window()
    
    def add_class(self, id_course, id_prof, name, schedule):
        return add_class(id_course, id_prof, name, schedule)
    
    def show_add_discipline(self):
        self.view.show_add_discipline_window()
    
    def add_discipline(self, id_course, date, begin, finish, local):
        return add_discipline(id_course, date, begin, finish, local)
    
    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    controller = AppController()
    controller.run()
