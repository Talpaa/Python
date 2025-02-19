#Exercise 4: University Management System

from typing import Any
from abc import ABC, abstractmethod

class Course:
    
    def __init__(self, 
                 course_name: str,
                 course_code: str) -> None:
        
        self.course_name: str = course_name.title()
        self.course_code: str = course_code.lower()
        self.students: list[Any] = []
        self.professor: Any = Any

    def add_student(self, student: Any):
        
        if student not in self.students:
            
            self.students.append(student)
            print(f'La matricola {student.student_id} è stata aggiunta al corso {self.course_name}')

        else:
            print(f'La matricola {student.student_id} è gia stata aggiunta al corso {self.course_name}')

    def set_professor(self, professor: Any):

        self.professor = professor

    def __str__(self) -> str:
        
        return f'Corso(Nome: {self.course_name}, Codice: {self.course_code})'


class Person(ABC):
    
    def __init__(self, 
                 name: str, 
                 age: int) -> None:
        
        self.name: str = name.title()
        self.age: int = age

    @abstractmethod
    def get_role(self, course: Course):
        pass

    def __str__(self) -> str:
        
        return f'Persona(nome: {self.name}, età: {self.age})'
    

class Student(Person):

    def __init__(self, 
                 name: str, 
                 age: int,
                 student_id: str) -> None:
        super().__init__(name, age)
        self.student_id: str = student_id.lower()
        self.courses: list[Course] = []

    def get_role(self, course: Course):
        
        if course not in self.courses:
            
            self.courses.append(course)
            print(f'La matricola {self.student_id} è stata iscitta al corso {course.course_name}')

        else:
            print(f'La matricola {self.student_id} è gia iscitto al corso {course.course_name}')
    

class Professor(Person):

    def __init__(self, 
                 name: str, 
                 age: int,
                 professor_id: str,
                 department: str) -> None:
        super().__init__(name, age)
        self.professor_id: str = professor_id.lower()
        self.department: str = department.title()
        self.courses: list[Course] = []

    def get_role(self, course: Course):
        
        if course not in self.courses:
            
            self.courses.append(course)
            print(f'Il professore {self.professor_id} è stata asseganato al corso {course.course_name}')

        else:
            print(f'Il professore {self.professor_id} è gia stato assegnato al corso {course.course_name}')


class Department:

    def __init__(self,
                 department_name: str,
                 ) -> None:
        
        self.department_name: str = department_name.title()
        self.courses: list[Course] = []
        self.professors: list[Professor] = []

    def add_course(self, course: Course):

        if course not in self.courses:
            
            self.courses.append(course)
            print(f'Il corso {course.course_name} ora fa parte del dipartimento di {self.department_name}')

        else:
            print(f'Il corso {course.course_name} gia fa parte del dipartimento di {self.department_name}')

    def add_professor(self, professor: Professor):
        
        if professor not in self.professors:
            
            self.professors.append(professor)
            print(f'Il professore {professor.professor_id} è stata asseganato al dipartimento di {self.department_name}')

        else:
            print(f'Il professore {professor.professor_id} è gia stato assegnato al dipartimento di {self.department_name}')

    def __str__(self) -> str:
        
        return f'Dipartimento(Nome: {self.department_name}, Numero Corsi: {len(self.courses)}, Numero Professori: {len(self.professors)})'
    
class University:
    
    def __init__(self, 
                 name: str) -> None:
        
        self.name: str = name.title()
        self.deparments: list[Department] = []
        self.students: list[Student] = []

    def add_department(self, department: Department):

        if department not in self.deparments:
            
            self.deparments.append(department)
            print(f'Il dipartimento di {department.department_name} ora fa parte dell\'università {self.name}')

        else:
            print(f'Il dipartimento di {department.department_name} già fa parte dell\'università {self.name}')

    def add_student(self, student: Student):

        if student not in self.students:
            
            self.students.append(student)
            print(f'La matricola {student.student_id} è stata iscitta all\'università {self.name}')

        else:
            print(f'La matricola {student.student_id} è gia iscitto all\'università {self.name}')

    def __str__(self) -> str:
        
        return f'Università(Nome: {self.name}, Numero Dipartimenti: {len(self.deparments)}, Numero Studenti: {len(self.students)})'
    

print()

Universita: University = University(name='Sapienza')

dipartimento: Department = Department(department_name='Ingegneria Informatica')
dipartimento1: Department = Department(department_name='Ingegneria civile')


corso: Course = Course(course_name=' PROGETTAZIONE DEL SOFTWARE', course_code='1018706')
corso1: Course = Course(course_name='ANALISI MATEMATICA I', course_code='1015374')


professore: Professor = Professor(name='Fabrizio Silvestri', age= 45, professor_id='B209', department='Ingegneria Informatica')
professore1: Professor = Professor(name='Silvio Fabrizi', age= 54, professor_id='E801', department='Ingegneria civile')


studente: Student = Student(name='Mario Rossi', age= 23, student_id='A101')
studente1: Student = Student(name='luigi verdi', age= 25, student_id='A102')
studente2: Student = Student(name='Wario Bianchi', age= 18, student_id='A103')
studente3: Student = Student(name='Pinco Pallino', age= 24, student_id='A105')
studente4: Student = Student(name='gino paoli', age= 90, student_id='A106')
studente5: Student = Student(name='Mario Rossi', age= 34, student_id='A107')
studente6: Student = Student(name='Mario Rossi', age= 22, student_id='A108')
studente7: Student = Student(name='Mario Rossi', age= 21, student_id='A109')
studente8: Student = Student(name='Mario Rossi', age= 27, student_id='A110')
studente9: Student = Student(name='Mario Rossi', age= 32, student_id='A111')



professore.get_role(course= corso)
professore1.get_role(course= corso1)

studente.get_role(course= corso)
studente1.get_role(course= corso1)
studente2.get_role(course= corso)
studente3.get_role(course= corso1)
studente4.get_role(course= corso)
studente5.get_role(course= corso1)
studente6.get_role(course= corso)
studente7.get_role(course= corso1)
studente8.get_role(course= corso)
studente9.get_role(course= corso1)


corso.add_student(student= studente)
corso.add_student(student= studente1)
corso.add_student(student= studente2)
corso.add_student(student= studente3)
corso.add_student(student= studente4)
corso1.add_student(student= studente5)
corso1.add_student(student= studente6)
corso1.add_student(student= studente7)
corso1.add_student(student= studente8)
corso1.add_student(student= studente9)


corso.set_professor(professor= professore)
corso1.set_professor(professor= professore1)


dipartimento.add_course(course= corso)
dipartimento1.add_course(course= corso1)

dipartimento.add_professor(professor= professore)
dipartimento1.add_professor(professor= professore1)



Universita.add_department(department= dipartimento)
Universita.add_department(department= dipartimento1)


Universita.add_student(student= studente )
Universita.add_student(student= studente1)
Universita.add_student(student= studente2)
Universita.add_student(student= studente3)
Universita.add_student(student= studente4)
Universita.add_student(student= studente5)
Universita.add_student(student= studente6)
Universita.add_student(student= studente7)
Universita.add_student(student= studente8)
Universita.add_student(student= studente9)



print(Universita)


