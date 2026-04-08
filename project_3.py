class library_managment_system:

    def __init__(self):

        self.books = {}
        self.borrow = {}
        self.user = {}

    def add_books(self, title, author, isbn, aval):

        self.books[isbn] = {
            "title": title,
            "author": author,
            "aval": aval
        }

    def register_user(self, name, id):

        self.user[id] = {
            'name': name
        }

    def issued_book(self, isbn, id):

        if isbn not in self.books:
            print("Book not found")
            return

        if self.books[isbn]["aval"] == False:
            print("Book not available")
            return

        self.borrow[isbn] = id
        self.books[isbn]["aval"] = False

        print("Book issued")

    def return_book(self, isbn, id):

        if isbn not in self.borrow:
            print("Book not borrowed")
            return

        if self.borrow[isbn] != id:
            print("Wrong user")
            return

        self.borrow.pop(isbn)
        self.books[isbn]["aval"] = True

        print("Book returned")

    def track_books(self):

        print("Borrowed books:", self.borrow)
lib = library_managment_system()

while True:

    print("1 Add Book\n2 Register User\n3 Issue Book\n4 Return Book\n5 Track Books\n6 Exit")

    ch = input("Enter choice: ")

    match ch:

        case "1":

            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")

            lib.add_books(title, author, isbn, True)

        case "2":

            name = input("User name: ")
            id = input("User id: ")

            lib.register_user(name, id)

        case "3":

            isbn = input("ISBN: ")
            id = input("User id: ")

            lib.issued_book(isbn, id)

        case "4":

            isbn = input("ISBN: ")
            id = input("User id: ")

            lib.return_book(isbn, id)

        case "5":

            lib.track_books()

        case "6":

            break

        case _:

            print("Invalid choice")