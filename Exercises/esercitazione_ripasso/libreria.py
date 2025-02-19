class Book:

    def __init__(self, book_id: str, title: str, author: str) -> None:
        
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False

    def borrow(self):

        if not(self.is_borrowed):

            self.is_borrowed = True

            return True
        
        else:

            return False

    def return_book(self):

        if self.is_borrowed:

            self.is_borrowed = False

            return True
        
        else:

            return False


class Member:

    def __init__(self, member_id, name: str) -> None:
        
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book):

        if book.borrow():

            self.borrowed_books.append(book)

    def return_book(self, book: Book):

        if (book.is_borrowed)and(book in self.borrowed_books):

            self.borrowed_books.remove(book)
            book.return_book()


class Library:

    def __init__(self) -> None:
        
        self.books: dict[str: Book] = {}
        self.members: dict[str: Member] = {}

    def add_book(self, book_id: str, title: str, author: str):

        book: Book = Book(book_id=book_id, title=title, author=author)

        self.books[book_id] = book

    def register_member(self, member_id:str, name: str):

        member: Member = Member(member_id=member_id, name=name)

        self.members[member_id] = member

    def borrow_book(self, member_id: str, book_id: str):

        if (member_id in self.members):
        
            if(book_id in self.books):

                if not(self.books[book_id].is_borrowed):
                
                    self.members[member_id].borrow_book(self.books[book_id])

                else:

                    print('Book is already borrowed')

            else:

                print('Book not found')

        else:

            print('Member not found')

    def return_book(self, member_id: str, book_id: str):

        if (member_id in self.members)and(book_id in self.books):

            if self.books[book_id] in self.members[member_id].borrowed_books:

                self.members[member_id].return_book(self.books[book_id])

            else:

                print('Book not borrowed by this member')

    def get_borrowed_books(self, member_id: str):

        if member_id in self.members:

            libri: list[str] = []

            for book in self.members[member_id].borrowed_books:

                self.return_book(member_id=member_id, book_id=book.book_id)

                libri.append(book.title)

            return libri
        


if __name__ == "__main__":




    library = Library()

    library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("B002", "1984", "George Orwell")
    library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

    # Register members
    library.register_member("M001", "Alice")
    library.register_member("M002", "Bob")
    library.register_member("M003", "Charlie")

    # Borrow books
    library.borrow_book("M001", "B001")
    library.borrow_book("M002", "B002")

    # Return books
    library.return_book("M001", "B001")
    library.return_book("M002", "B002")

    # Edge case - trying to return a book that is not borrowed
    try:
        library.return_book("M001", "B003")
    except ValueError as e:
        print(e)