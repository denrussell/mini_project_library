# This will hold all operations related to books

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True
            
    
    def get_details(self):
        return {
            "Title" : self.__title,
            "Author" : self.__author,
            "Genre" : self.__genre,
            "Publication Date" : self.__publication_date,
            "Available" : self.__is_available,
        }

    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False
        
    
    def return_book(self):
        self.__is_available = True

    def add_book(library, authors):
        title = input("Enter the title of the book: ")
        author = input("Enter the name of the author: ")
        genre = input("Enter the genre: ")
        publication_date = input("Enter the publication date: ")

        if author not in authors:
            print(f"Author does not exist. Please add author first.")
            return
        
        if title in library:
            print("Book already exists in the library.")
        
        else:
            book = Book(title, genre, publication_date, author)
            library[title] = book
            print(f"\n>>>> Book '{title}' by  has by {author} has been added successfully.")

    def search_book(library, title):
        if title in library:
            details = library[title].get_details()
            print(f"\nTitle: {details['Title']}")
            print(f"Author: {details['Author']}")
            print(f"Genre: {details['Genre']}")
            print(f"Publication Date: {details['Publication Date']}")
            print(f"Available: {'Yes' if details['Available'] else 'No'}")

        else:
            print("Book not found.")
    
    def display_all_books(library):
        if not library:
            print("\n>>>> No books available in the library.")
        else:
            print("\nAll books in the library:\n")
            for title, book in library.items():
                details = book.get_details()
                print(f"Title: {details['Title']}")
                print(f"Genre: {details['Genre']}")
                print(f"Publication Date: {details['Publication Date']}")
                print(f"Author: {details['Author']}")
                print(f"Available: {'Yes' if details['Available'] else 'No'}")
                print("-" * 40)

'''    
def checkout_book(library, current_loans):
    title = input("Enter the title of the book to borrow: ")
    user = input("Enter user name: ")
    if title in library and library[title].borrow_book():
        current_loans[title] = user
        print(f"Book {library[title].get_title()} checked out to {user}.")
    else:
        print("Book not available or not found.")  

def checkin_book(library, current_loans):
    title = input("Enter title of the book to return: ")
    if title in library and title in current_loans:
        library[title].return_book()
        del current_loans[title]
        print(f"Book '{library[title].get_title()}")
    else:
        print("Invalid title or the book was not borrowed.")
'''
'''
def main():
    library = {}
    current_loans = {}
    while True:
        print("1. Add a new book")
        print("2. Borrow a book")
        print("Return a book")
        print("Search for a book")
        print("Display all books")

        choice = input("Enter choice number: ")
        try:
            if choice == "1":
                add_book(library)
            elif choice == "2":
                checkout_book(library, current_loans)
            elif choice == "3":
                checkin_book(library, current_loans)
            elif choice == "4":
                search_book(library)
            elif choice == "5":
                display_all_books(library)
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

'''
'''
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_publication(self):
        return self.__publication_date
'''