# This is what you will run

from book_operations import Book
from user_operations import User, add_user, display_all_users
from author_operations import Author, add_author, display_all_authors, get_author_details
from user_interface import main_menu, book_menu, user_menu, author_menu

def main():
    library = {}
    users = {}
    authors = {}

    while True:
        main_menu()
        choice = input("Enter choice number: ")
        if choice == "1":
            while True:
                book_menu()
                book_choice = input("Enter choice number: ")
                if book_choice == "1":
                    Book.add_book(library, authors)
                elif book_choice == "2":
                    title = input("Enter the title of the book to borrow: ")
                    library_id = input("Enter the user's Library ID: ")

                    
                    #user = input("Enter user name: ")
                    if title in library and library_id in users:
            
                        book = library[title]
                        user = users[library_id]

                        if book.borrow_book():
                            user.borrow_book(title)
                            print(f"Book '{title}' has been borrowed by {user.get_user_details()['Name']}.")
                       
                        else:
                            print("\n>>>> Book not available or not found.")
                    else:
                        print("Invalid book title or Library ID.")  
                
                elif book_choice == "3":
                    title = input("Enter title of the book to return: ")
                    library_id = input("Enter the user's Library ID: ")

                    if title in library and library_id in users:
                        book = library[title]
                        user = users[library_id]

                        book.return_book()
                        user.return_book(title)
                        print(f"Book '{title}' has been returned by {user.get_user_details()['Name']}")
                     
                    else:
                        print("\n>>>> Invalid title or invalid library ID or the book was not borrowed.")
                elif book_choice == "4":
                    title = input("Enter the title of the book: ")
                    Book.search_book(library, title)
                elif book_choice == "5":
                    Book.display_all_books(library)
                elif book_choice == "6":
                    print("Returning to the Main Menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "2":
            while True:
                user_menu()
                user_choice = input("Enter choice number: ")
                
                if user_choice == "1":
                    add_user(users)  # add user
                elif user_choice == "2":
                    library_id = input("Enter the user's library ID: ")
                    if library_id in users:
                        user = users[library_id]
                        details = user.get_user_details()
                        print(f"\nName: {details['Name']}")
                        print(f"Library ID: {details['Library_ID']}")
                        print(f"Borrowed Books: {', '.join(details['Borrowed_Books']) if details['Borrowed_Books'] else 'None'}")
                    else:
                        print("User not found.")
                elif user_choice == "3":
                    display_all_users(users) # view all users
                elif user_choice == "4":
                    print("Returning to the Main Menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "3":
            while True:
                author_menu()
                author_choice = input("Enter choice number: ")

                if author_choice == "1":
                    add_author(authors)
                elif author_choice == "2":
                    get_author_details(authors)
                elif author_choice == "3":
                    display_all_authors(authors)
                elif author_choice == "4":
                    print("Returning to the Main Menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid. Please try again.")
            
if __name__ == "__main__":
    main()