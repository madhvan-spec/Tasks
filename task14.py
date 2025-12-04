import json
import os

FILENAME = "task14.json"

class Book:
    book_id_counter = 0
    def __init__(self,title,author,genre):
        Book.book_id_counter +=1
        self.book_id = f"B{Book.book_id_counter}"
        self.title = title
        self.author = author
        self.genre = genre

    def get_book_details(self):
        print("----Book Details----")
        print(f"ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}")

    def to_json(self):
        return{
            "book_id" : self.book_id,
            "title" : self.title,
            "author" : self.author,
            "genre" : self.genre
        }
    
    @staticmethod
    def from_json(data):
        book = Book.__new__(Book)   
        book.book_id = data["book_id"]
        book.title = data["title"]
        book.author = data["author"]
        book.genre = data["genre"]
        return book
    
class BookCopy:
    def __init__(self, copy_id, book_id, library_id, is_available=True, borrowed_by=None):
        self.copy_id = copy_id
        self.book_id = book_id        
        self.library_id = library_id
        self.is_available = is_available
        self.borrowed_by = borrowed_by

    def to_json(self):
        return {
            "copy_id": self.copy_id,
            "book_id": self.book_id,   
            "library_id": self.library_id,
            "is_available": self.is_available,
            "borrowed_by": self.borrowed_by
        }

    @staticmethod
    def from_json(data, books_dict):
        
        return BookCopy(
            data["copy_id"],
            data["book_id"],       
            data["library_id"],
            data["is_available"],
            data["borrowed_by"]
        )

    
class Member:
    member_id_counter = 0
    def __init__(self,name,library_id):
        Member.member_id_counter +=1
        self.member_id = f"M{Member.member_id_counter}"
        self.name = name
        self.library_id = library_id
        self.borrowed_copies = []

    
    def to_json(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "library_id": self.library_id,
            "borrowed_copies": self.borrowed_copies
        }

    @staticmethod
    def from_json(data):
        member = Member.__new__(Member)
        member.member_id = data["member_id"]
        member.name = data["name"]
        member.library_id = data["library_id"]
        member.borrowed_copies = data["borrowed_copies"]

        return member


class Library:
    library_id_counter = 0
    def __init__(self,name):
        Library.library_id_counter += 1
        self.library_id = f"L{Library.library_id_counter}"
        self.name = name
        self.books = {}
        self.copies = {}
        self.members = {}

    def to_json(self):
        return{
            "library_id" : self.library_id,
            "name" : self.name,
            "books" : self.books,
            "copies" : self.copies,
            "members" : self.members
        }

    @staticmethod
    def from_json(data):
        library = Library(data["name"])
        library.library_id = data["library_id"]
        library.books = data["books"]
        library.copies = data["copies"]
        library.members = data["members"]
        
        return library


class LibrarySystem:

    books = {}
    libraries = {}
    members = {}
    book_copies = {}
    book_copy_counters = {}

    def __init__(self):
        self.load_data()

    
    def save_data(self):
        data = {
            "books": {book_id: book.to_json() for book_id, book in self.books.items()},
            "members": {member_id: member.to_json() for member_id, member in self.members.items()},
            "book_copies": {copy_id: copy.to_json() for copy_id, copy in self.book_copies.items()},
            "libraries": {
                lib_id: {
                    "library_id": lib.library_id,
                    "name": lib.name,
                    "books": list(lib.books.keys()),    
                    "copies": list(lib.copies.keys()),  
                    "members": list(lib.members.keys()) 
                } for lib_id, lib in self.libraries.items()
            },
            "counters": {
                "book_id_counter": Book.book_id_counter,
                "member_id_counter": Member.member_id_counter,
                "library_id_counter": Library.library_id_counter,
                "book_copy_counters": getattr(self, "book_copy_counters", {})
            }
        }

        with open(FILENAME, 'w') as f:
            json.dump(data, f, indent=4)


    def load_data(self):
        if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
            return

        with open(FILENAME, 'r') as f:
            data = json.load(f)

        if not data:
            return

        # Restore counters
        Book.book_id_counter = data['counters'].get('book_id_counter', 0)
        Member.member_id_counter = data['counters'].get('member_id_counter', 0)
        Library.library_id_counter = data['counters'].get('library_id_counter', 0)
        self.book_copy_counters = data['counters'].get('book_copy_counters', {})

        # Load books
        self.books = {book_id: Book.from_json(book_data) for book_id, book_data in data.get("books", {}).items()}

        # Load members
        self.members = {member_id: Member.from_json(member_data) for member_id, member_data in data.get("members", {}).items()}

        # Load book copies
        self.book_copies = {copy_id: BookCopy.from_json(copy_data, self.books)
                            for copy_id, copy_data in data.get("book_copies", {}).items()}

        # Load libraries (with IDs only)
        self.libraries = {}
        for lib_id, lib_data in data.get("libraries", {}).items():
            library = Library.__new__(Library)
            library.library_id = lib_data["library_id"]
            library.name = lib_data["name"]
            library.books = {bid: bid for bid in lib_data.get("books", [])}       
            library.copies = {cid: cid for cid in lib_data.get("copies", [])}     
            library.members = {mid: mid for mid in lib_data.get("members", [])}   
            self.libraries[lib_id] = library





    def print_file_data(self):
        if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
            return
        with open(FILENAME , 'r') as f:
            data = json.load(f)
            if data :
                print(data)
            else:
                print("File is Empty")
        

    def add_books(self):
        title = input("Please Enter the title of the Book: ")
        author = input("Please Enter the Author of the Book: ")
        genre = input("Please Enter the Genre of the Book: ")
        b1 = Book(title,author,genre)
        self.books[b1.book_id] = b1

    def add_library(self):
        name = input("Enter Library Name: ")
        l1 = Library(name)
        self.libraries[l1.library_id] = l1


    def member_login_or_register(self):
        if not self.libraries:
            print("No libraries available. Please add a library first.")
            return None, None

        
        print("Available Libraries:")
        for lib_id, lib in self.libraries.items():
            print(f"{lib_id}: {lib.name}")
        
        chosen_lib_id = input("Enter Library ID to enter: ").strip()
        if chosen_lib_id not in self.libraries:
            print("Invalid library ID.")
            return None, None

        library = self.libraries[chosen_lib_id]

        
        print("\n1. Login as existing member")
        print("2. Become a new member")
        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":
            member_id = input("Enter your Member ID: ").strip()
            if member_id in library.members:
               member = self.members.get(member_id)
               if member:
                print(f"Welcome back, {member.name}!")
                return library, member
               else:
                   print("Member not found")
                   
            else:
                print("Member ID not found in this library.")
                return None, None

        elif choice == "2":
            name = input("Enter your name to become a new member: ").strip()
            member = Member(name, library.library_id)
            library.members[member.member_id] = member
            self.members[member.member_id] = member
            print(f"Welcome {name}! Your Member ID is {member.member_id}")
            return library, member

        else:
            print("Invalid choice.")
            return None, None
        
    
    def add_book_copy(self):
        if not self.libraries:
            print("No libraries available. Add a library first.")
            return
        if not self.books:
            print("No books available. Add a book first.")
            return

      
        print("\nAvailable Libraries:")
        for lib_id, lib in self.libraries.items():
            print(f"{lib_id}: {lib.name}")
        chosen_lib_id = input("Enter Library ID to add copies: ").strip()
        if chosen_lib_id not in self.libraries:
            print("Invalid library ID.")
            return
        library = self.libraries[chosen_lib_id]

       
        print("\nAvailable Books:")
        for book_id, book in self.books.items():
            print(f"{book_id}: {book.title} by {book.author}")
        chosen_book_id = input("Enter Book ID to add copies for: ").strip()
        if chosen_book_id not in self.books:
            print("Invalid book ID.")
            return
        book = self.books[chosen_book_id]

        
        try:
            num_copies = int(input("Enter number of copies to add: ").strip())
        except ValueError:
            print("Invalid number.")
            return

        
        if not hasattr(self, "book_copy_counters"):
            self.book_copy_counters = {}
        if chosen_book_id not in self.book_copy_counters:
            self.book_copy_counters[chosen_book_id] = 0

        
        for _ in range(num_copies):
            self.book_copy_counters[chosen_book_id] += 1
            copy_id = f"{chosen_book_id}_Copy{self.book_copy_counters[chosen_book_id]}"
            copy = BookCopy(copy_id, book.book_id, library.library_id)  
            self.book_copies[copy_id] = copy
            library.copies[copy_id] = copy_id  

        print(f"{num_copies} copies of '{book.title}' added to {library.name}.")
    
    def borrow_book(self, library, member):
        
        available_books = {}
        for copy_id in library.copies:
            copy = self.book_copies[copy_id]
            if copy.is_available and copy.book_id not in [self.book_copies[cid].book_id for cid in member.borrowed_copies]:
                available_books[copy.book_id] = self.books[copy.book_id]

        if not available_books:
            print("No available books to borrow at the moment.")
            return

        print("\nAvailable Books to Borrow:")
        for book_id, book in available_books.items():
            print(f"{book_id}: {book.title} by {book.author}")

        chosen_book_id = input("Enter Book ID to borrow: ").strip()
        if chosen_book_id not in available_books:
            print("Invalid Book ID or you already borrowed a copy of this book.")
            return

        
        for copy_id in library.copies:
            copy = self.book_copies[copy_id]
            if copy.book_id == chosen_book_id and copy.is_available:
                copy.is_available = False
                copy.borrowed_by = member.member_id
                member.borrowed_copies.append(copy.copy_id)
                print(f"You have successfully borrowed '{self.books[chosen_book_id].title}'.")
                self.save_data()
                return

    
    def return_book(self, member):
        if not member.borrowed_copies:
            print("You have no borrowed books to return.")
            return

        print("\nYour Borrowed Books:")
        for idx, copy_id in enumerate(member.borrowed_copies, start=1):
            copy = self.book_copies[copy_id]
            book = self.books[copy.book_id]
            print(f"{idx}. {copy.copy_id}: {book.title} by {book.author}")

        try:
            choice = int(input("Enter the number of the book to return: ").strip())
            if choice < 1 or choice > len(member.borrowed_copies):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input.")
            return

        copy_id = member.borrowed_copies.pop(choice - 1)
        copy = self.book_copies[copy_id]
        copy.is_available = True
        copy.borrowed_by = None
        print(f"You have successfully returned '{self.books[copy.book_id].title}'.")
        self.save_data()





        

        
def main_menu():
    library_system = LibrarySystem()
    
    while True:
        print("\n--- Welcome to the Library System ---")
        print("1. Member Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library, member = library_system.member_login_or_register()
            if member:
                member_menu(library_system, library, member)

        elif choice == "2":
            admin_password = "admin123" 
            password = input("Enter admin password: ").strip()
            if password == admin_password:
                print("Admin login successful!")
                admin_menu(library_system)
            else:
                print("Incorrect password!")

        elif choice == "3":
            print("Exiting... Goodbye!")
            library_system.save_data()
            break
        else:
            print("Invalid choice. Please try again.")

def member_menu(system, library, member):
    while True:
        print(f"\n--- Member Menu ({member.name}) ---")
        print("1. View My Borrowed Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            if member.borrowed_copies:
                print("Your Borrowed Books:")
                for copy_id in member.borrowed_copies:
                    copy = system.book_copies.get(copy_id)
                    book = system.books[copy.book_id]
                    print(f"{copy.copy_id}: {book.title} by {book.author}")
            else:
                print("You have not borrowed any books yet.")

        elif choice == "2":
            system.borrow_book(library, member)

        elif choice == "3":
            system.return_book(member)

        elif choice == "4":
            print(f"Goodbye, {member.name}!")
            break

        else:
            print("Invalid choice. Try again.")



def admin_menu(system):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Book")
        print("2. Add Library")
        print("3. Add Book Copies")
        print("4. View Data File")
        print("5. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            system.add_books()
            system.save_data()
        elif choice == "2":
            system.add_library()
            system.save_data()
        elif choice == "3":
            system.add_book_copy()
            system.save_data()
        elif choice == "4":
            system.print_file_data()
        elif choice == "5":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Try again.")




main_menu()





