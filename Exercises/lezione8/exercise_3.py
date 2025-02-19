#Exercise 3: Library Management System 

class Book:

    def __init__(self, 
                 title: str,
                 autor: str, 
                 isbn: str) -> None:
        
        self.title: str = title.title()
        self.autor = autor.title()
        self.isbn = isbn
        self.available: bool = True

    def __str__(self) -> str:
        
        return f'Il titolo del libro è {self.title} è sato scritto da {self.autor} e il suo codice isbn è {self.isbn}.\n'
    
    @classmethod
    def from_string(cls, book_str: str):

        #book_str = "title, author, isbn"
        i: int = 0
        title: str = ''
        autor: str = ''
        isbn: str = ''

        for char in book_str:

            if (char == ','):

                i += 1

            elif (char != ',')and(i == 0):

                title += char

            elif (char != ',')and(i == 1):

                autor += char

            elif (char != ',')and(i == 2):

                isbn += char

        title = title.title()
        autor = autor.title()

        return cls(title, autor, isbn)
    
class Member:

    def __init__(self, 
                 name: str, 
                 member_id: str) -> None:
        
        self.name = name.title()
        self.member_id = member_id
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book):

        self.borrowed_books.append(book)

        print(f'Il libro {book.title} di {book.autor} è stato aggiunto alla lista dei libri presi in prestito.\n')

    def remove_book(self, book: Book):

        if book in self.borrowed_books:

            self.borrowed_books.remove(book)

    def __str__(self) -> str:
    
        return f'Il nome del titolare della tessera {self.member_id} è {self.name} e attualmente sta leggendo {len(self.borrowed_books)} libri.\n'
    
    @classmethod
    def from_string(cls, member_str: str):

        #book_str = "title, author, isbn"
        i: int = 0
        name: str = ''
        member_id: str = ''

        for char in member_str:

            if (char == ','):

                i += 1

            elif (char != ',')and(i == 0):

                name += char

            elif (char != ',')and(i == 1):

                member_id += char

        name = name.title()
        member_id = member_id.title()

        return cls(name, member_id)
    
class Library:

    total_books: int = 0

    def __init__(self) -> None:
        
        self.books: list[Book]= []
        self.members: list[Member] = []

    def add_books(self, book: Book):

        self.books.append(book)

        print(f'Il libro {book.title} di {book.autor} è stato aggiunto alla libreria.\n')

        Library.total_books += 1

    def remove_book(self, book: Book):

        if book in self.books:

            self.books.remove(book)
            print(f'Il libro {book.title} di {book.autor} è stato rimosso dalla libreria.\n')

            Library.total_books -= 1

        else:

            print(f'Il libro {book.title} di {book.autor} non è presente nella libreria.\n')

    def register_member(self, member: Member):

        self.members.append(member)

        print(f'La tessera {member.member_id} è stata assegnata a {member.name}.\n')

    def lend_book(self, book: Book, member: Member):

        if book in self.books:

            if member in self.members:

                if book.available:


                    print(f'Il libro {book.title} di {book.autor} è stato preso in prestito da {member.name} ID {member.member_id}.\n')

                else:

                    print(f'Il libro {book.title} di {book.autor} non è attualmente presente nella libreria.\n')
            else:

                print(f'ID {member.member_id} non riconosciuto')

        else:

            print(f'Il libro {book.title} di {book.autor} non è presente nella libreria.\n')

    def return_book(self, book: Book, member: Member):

        if book in self.books:

            if member in self.members:

                if not(book.available):


                    print(f'Il libro {book.title} di {book.autor} è stato restituito da {member.name} ID {member.member_id}.\n')

            else:

                print(f'ID {member.member_id} non riconosciuto')

        else:

            print(f'Il libro {book.title} di {book.autor} non fa parte di questa libreria.\n')

    def __str__(self) -> str:

        num_books: int = 0

        message: str = f''

        if len(self.books) > 0:
            
            message = f'Ecco la lista di tutti i libri presenti nella libreria:\n'

            for book in self.books:

                num_books += 1

                message = message + f'{num_books}) {book.__str__()}'

        else:

            message = f'Non sono presenti libri in questa libreria.'

        num_members: int = 0

        if len(self.members) > 0:
            
            message = message + f'\n\nEcco la lista di tutti i tesserati della libreria:\n'

            for member in self.members:

                num_members += 1

                message = message + f'{num_members}) {member.__str__()}'

        else:

            message = message + f'\n\nNon sono presenti tesserati in questa libreria.\n'
        
        return message
    
    @classmethod
    def library_statistics(cls):

        if cls.total_books > 1:
            print(f'Il numero totale di libri presenti nella libreria sono: {cls.total_books}.\n')

        else:
            print(f'Il numero totale di libri presenti nella libreria è: {cls.total_books}.\n')


        
print()
print()

#Creazione dell' istanza libreria
libreria: Library = Library()

print(libreria)


#creazione dell'istanza libro da stringa fotmatatta "title, author, isbn"
book: str = 'La Divina Commedia,Dante Alighieri,999000666'
divina_commedia: Book = Book.from_string(book)

print(divina_commedia)


#creazione dell'istanza tesserato alla biblioteca da stringa fotmatatta "name,member_id"
tesserato: str = 'Francesco,999000666'
francesco: Member = Member.from_string(tesserato)

print(francesco)

libreria.add_books(book=divina_commedia)

print(libreria)

libreria.register_member(member=francesco)

print(libreria)

#creazione dell'istanza libro da stringa fotmatatta "title, author, isbn"
book: str = 'tuttu le barzellette su Totti,Francesco Totti,999000666'
francesco_totti: Book = Book.from_string(book)

libreria.add_books(book= francesco_totti)

Library.library_statistics()

libreria.remove_book(divina_commedia)

Library.library_statistics()
