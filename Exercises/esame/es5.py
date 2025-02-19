class Student:

    def __init__(self, student_id: str) -> None:
        
        self.student_id: str = student_id
        self.courses: list[str] = []

    def enroll(self, course: str)->None:

        if course in self.courses:

            print(f'Lo studente è già iscritto al corso {course}.')

        else:

            self.courses.append(course)

    def get_courses(self)->list[str]:

        return self.courses
    

class School:

    def __init__(self) -> None:
        
        self.students: dict[str: Student] = {}

    def create_student(self, student_id: str)->None:

        if student_id in self.students:

            print(f'Lo studente con ID {student_id} esiste già.')

        else: 

            student: Student = Student(student_id=student_id)

            self.students[student_id] = student

    def enroll_student(self, student_id: str, course: str)->None:
        
        if student_id in self.students:

            self.students[student_id].enroll(course)

        else:

            print(f'Studente non trovato.')

    def get_student_courses(self, student_id: str)->None|str:

        if student_id in self.students:

            return self.students[student_id].get_courses()
        
        else:

            return f'Studente non trovato.'
        
    def get_student_list(self)->list[str]:

        lista: list = []

        for key in self.students:

            lista.append(key)

        return lista
    
    def search_by_course(self, course: str)->list[str]|str:

        flag: bool = False

        if self.students:

            lista: list[str] = []
            
            for key in self.students:

                if course in self.students[key].courses:

                    lista.append(key)
                    flag = True

        if flag:

            return lista

        else:
            
            return f'Nessuno studente è iscritto al corso {course}.'
        
 	

# Creazione di una nuova scuola
scuola = School()

# Creazione di nuovi studenti
scuola.create_student("1001")
scuola.create_student("1002")
scuola.create_student("1003")

# Iscrizione degli studenti ai corsi
scuola.enroll_student("1001", "Matematica")
scuola.enroll_student("1002", "Fisica")
scuola.enroll_student("1003", "Chimica")

# Elenco di tutti gli studenti registrati
print(scuola.get_student_list())