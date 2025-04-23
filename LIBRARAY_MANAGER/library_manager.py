
#  Advanced Library Management System in Python
#  before running this code, make sure to install colorama using pip install colorama --force

# 📦 Importing necessary modules
import json       # For saving and loading data in JSON format
import os         # To check if the file exists
import sys        # To make sure output shows up before exit
from colorama import init, Fore, Style  # For colored output

# Initialize colorama for colored text in the terminal
init(autoreset=True)

# 📁 File where all book records will be stored
LIBRARY_FILE = "library.json"

# 🧾 Function to load the book library from the file (if it exists)
def load_library():
    # Check if the library file exists
    if os.path.exists(LIBRARY_FILE):
        # Open the file and load the data
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    # If the file doesn't exist, return an empty list (no books)
    return []

# 💾 Function to save the current library (list of books) to the file
def save_library(library):
    # Open the library file and save the current data
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# 📘 Function to get non-empty input from the user
def get_non_empty_input(prompt):
    while True:
        # Ask the user for input
        value = input(prompt).strip()
        if value:
            return value
        # If input is empty, show a warning message
        print(Fore.YELLOW + "⚠ This field cannot be empty. Please enter again.")

# 📅 Function to get valid year input from user
def get_valid_year(prompt):
    while True:
        # Ask for the year and remove any extra spaces
        year = input(prompt).strip()
        # Check if the input is a number (valid year)
        if year.isdigit():
            return year
        # If the input is not a valid number, show a warning message
        print(Fore.YELLOW + "⚠ Please enter a valid year (numbers only).")

# 🧾 Function to print a nice welcome message at the top
def print_header():
    print(Fore.CYAN + "╔════════════════════════════════════════════════╗")
    print("║        📚 Welcome to Personal Library!         ║")
    print("║         Manage your books like a pro! 🎯        ║")
    print("╚════════════════════════════════════════════════╝")

# 🖋 Function to print a goodbye/footer message at the end
def print_footer():
    print(Fore.CYAN + "╔════════════════════════════════════════════════╗")
    print("║ ✍ Made by: Muhammad Hammad Zubair             ║")
    print("║ 🐍 Powered by Python                          ║")
    print("╚════════════════════════════════════════════════╝\n")
    sys.stdout.flush()

# ➕ Function to add a new book to the library
def add_book(library):
    print("\n📘 Add a New Book")
    title = get_non_empty_input("📖 Enter Book Title: ")
    author = get_non_empty_input("✍ Enter Author Name: ")
    year = get_valid_year("📅 Enter Publication Year: ")
    genre = get_non_empty_input("📂 Enter Book Genre: ")
    read = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"

    # Create a dictionary to store the book details
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    # Add the new book to the library
    library.append(book)
    # Save the updated library to the file
    save_library(library)
    print(Fore.GREEN + f"\n✅ '{title}' added successfully!\n")

# ❌ Function to remove a book by matching its title
def remove_book(library):
    print("\n🗑 Remove a Book")
    title = get_non_empty_input("📖 Enter the title to remove: ")
    # Loop through each book in the library
    for book in library:
        # If the title matches, remove the book
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print(Fore.RED + f"\n❌ '{title}' removed successfully!\n")
            return
    # If book is not found, show a warning message
    print(Fore.YELLOW + "\n⚠ Book not found!\n")

# 🔍 Function to search for a book by title
def search_book(library):
    print("\n🔍 Search for a Book")
    title = get_non_empty_input("📖 Enter the title to search for: ")
    # Loop through each book to find the matching title
    for book in library:
        if book["title"].lower() == title.lower():
            print("\n📖 Book Found:")
            print_book(book)
            return
    # If book is not found, show a warning message
    print(Fore.YELLOW + "\n⚠ Book not found!\n")

# 📚 Function to list all books in the library
def list_books(library):
    # If the library is empty, show a warning message
    if not library:
        print(Fore.YELLOW + "\n📚 Your library is empty!\n")
        return
    print("\n📚 Your Book Collection:")
    # Loop through each book and display it
    for idx, book in enumerate(library, start=1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
    print()

# 🔁 Function to toggle the read/unread status of a book
def update_read_status(library):
    print("\n🔄 Update Read Status")
    title = get_non_empty_input("📖 Enter the book title: ")
    # Loop through each book to find the matching title
    for book in library:
        if book["title"].lower() == title.lower():
            # Toggle the read status
            book["read"] = not book["read"]
            save_library(library)
            status = "Read" if book["read"] else "Not Read"
            print(Fore.GREEN + f"\n✅ '{title}' marked as {status}.\n")
            return
    # If book is not found, show a warning message
    print(Fore.YELLOW + "\n⚠ Book not found!\n")

# 📊 Function to show library statistics
def show_statistics(library):
    # Calculate total books, read books, and unread books
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    unread_books = total_books - read_books

    print("\n📊 Library Statistics:")
    print(f"📚 Total Books: {total_books}")
    print(f"✅ Books Read: {read_books}")
    print(f"❌ Books Unread: {unread_books}\n")

# 📝 Function to print one book's details
def print_book(book):
    print(f"\n📖 Title: {book['title']}")
    print(f"✍ Author: {book['author']}")
    print(f"📅 Year: {book['year']}")
    print(f"📂 Genre: {book['genre']}")
    print(f"📘 Read: {'✅ Yes' if book['read'] else '❌ No'}\n")

# 🗂 Function to sort books by title, year, or read status
def sort_books(library):
    print("\n🔃 Sort Books By:")
    print("1️⃣ Title")
    print("2️⃣ Year")
    print("3️⃣ Read Status")
    choice = input("➡ Choose an option (1-3): ").strip()
    # Sort books based on the user's choice
    if choice == "1":
        sorted_books = sorted(library, key=lambda b: b['title'].lower())
    elif choice == "2":
        sorted_books = sorted(library, key=lambda b: b['year'])
    elif choice == "3":
        sorted_books = sorted(library, key=lambda b: b['read'], reverse=True)
    else:
        print(Fore.YELLOW + "⚠ Invalid option.\n")
        return
    print("\n📚 Sorted Book Collection:")
    # Display the sorted list of books
    for idx, book in enumerate(sorted_books, start=1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
    print()

# 📤 Function to export library to a TXT file
def export_books_txt(library):
    # If the library is empty, show a warning message
    if not library:
        print(Fore.YELLOW + "\n⚠ Library is empty. Nothing to export.\n")
        return

    filename = "library_export.txt"
    # Open the file to write the book details
    with open(filename, "w", encoding="utf-8") as file:
        for book in library:
            file.write(f"Title: {book['title']}\n")
            file.write(f"Author: {book['author']}\n")
            file.write(f"Year: {book['year']}\n")
            file.write(f"Genre: {book['genre']}\n")
            file.write(f"Read: {'Yes' if book['read'] else 'No'}\n")
            file.write("-" * 40 + "\n")

    # Show a success message
    print(Fore.GREEN + f"\n📤 Library exported to {filename} successfully!\n")

# 🧭 Main menu function
def main():
    # Load the library from the file
    library = load_library()
    # Print the header message
    print_header()

    # Show the main menu and allow the user to make choices
    while True:
        print("\n📚 Main Menu")
        print("1️⃣ Add a Book")
        print("2️⃣ Remove a Book")
        print("3️⃣ Search for a Book")
        print("4️⃣ List All Books")
        print("5️⃣ Mark Book as Read/Unread")
        print("6️⃣ Show Statistics")
        print("7️⃣ Sort Books")
        print("8️⃣ Export Library to TXT")
        print("9️⃣ Exit")

        choice = input("\n➡ Enter your choice (1-9): ").strip()

        # Call the corresponding function based on user input
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            list_books(library)
        elif choice == "5":
            update_read_status(library)
        elif choice == "6":
            show_statistics(library)
        elif choice == "7":
            sort_books(library)
        elif choice == "8":
            export_books_txt(library)
        elif choice == "9":
            # Print footer and exit the program
            print_footer()
            print("\n👋 Goodbye! Happy Reading!\n")
            break
        else:
            print(Fore.YELLOW + "\n⚠ Invalid choice! Please enter a number from 1 to 9.\n")

# 🚀 Start the program from here
if __name__ == "__main__":
    main()



# # 📚 Basic Library Management System in Python

# # 📦 Importing necessary modules
# import json       # To save and load book data in JSON format
# import os         # To check if the file exists

# # 📁 File to store book records
# LIBRARY_FILE = "library.json"

# # 🧾 Function to load books from the file (if it exists)
# def load_library():
#     if os.path.exists(LIBRARY_FILE):  # Check if the file exists
#         with open(LIBRARY_FILE, "r") as file:
#             return json.load(file)  # Read and return the data
#     return []  # If file doesn't exist, return an empty list

# # 💾 Function to save the library (list of books) to the file
# def save_library(library):
#     with open(LIBRARY_FILE, "w") as file:
#         json.dump(library, file, indent=4)  # Save with nice formatting

# # ➕ Function to add a new book to the library
# def add_book(library):
#     print("\n📘 Add a New Book")
#     title = input("📖 Enter Book Title: ").strip()  # Get book title
#     author = input("✍ Enter Author Name: ").strip()  # Get author name
#     year = input("📅 Enter Publication Year: ").strip()  # Get year
#     genre = input("📂 Enter Genre: ").strip()  # Get genre
#     read = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"  # Ask if read

#     # Create a dictionary for the new book
#     book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "genre": genre,
#         "read": read
#     }

#     library.append(book)  # Add the new book to the list
#     save_library(library)  # Save the updated list
#     print(f"\n✅ '{title}' added successfully!\n")

# # ❌ Function to remove a book by its title
# def remove_book(library):
#     print("\n🗑 Remove a Book")
#     title = input("📖 Enter the title to remove: ").strip()  # Get the title to remove
#     for book in library:
#         if book["title"].lower() == title.lower():  # Case-insensitive match
#             library.remove(book)
#             save_library(library)
#             print(f"\n❌ '{title}' removed successfully!\n")
#             return
#     print("\n⚠ Book not found!\n")  # If no match found

# # 🔍 Function to search for a book by its title
# def search_book(library):
#     print("\n🔍 Search for a Book")
#     title = input("📖 Enter the title to search: ").strip()  # Get the title to search
#     for book in library:
#         if book["title"].lower() == title.lower():  # Case-insensitive match
#             print("\n📖 Book Found:")
#             print_book(book)  # Display book details
#             return
#     print("\n⚠ Book not found!\n")  # If book not found

# # 📚 Function to list all books in the library
# def list_books(library):
#     if not library:  # If the library is empty
#         print("\n📚 Your library is empty!\n")
#         return
#     print("\n📚 Your Book Collection:")
#     # Show all books with numbers
#     for idx, book in enumerate(library, start=1):
#         print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Not Read'}")
#     print()

# # 🔄 Function to update the read/unread status of a book
# def update_read_status(library):
#     print("\n🔄 Update Read Status")
#     title = input("📖 Enter the book title: ").strip()  # Get title to update
#     for book in library:
#         if book["title"].lower() == title.lower():  # Match the title
#             book["read"] = not book["read"]  # Toggle the read/unread status
#             save_library(library)
#             status = "Read" if book["read"] else "Not Read"
#             print(f"\n✅ '{title}' marked as {status}.\n")
#             return
#     print("\n⚠ Book not found!\n")  # If no match found

# # 📊 Function to show library statistics (read/unread books)
# def show_statistics(library):
#     total_books = len(library)  # Total number of books
#     read_books = sum(1 for book in library if book["read"])  # Count the read books
#     unread_books = total_books - read_books  # Remaining books are unread

#     print("\n📊 Library Stats:")
#     print(f"📚 Total Books: {total_books}")
#     print(f"✅ Books Read: {read_books}")
#     print(f"❌ Books Unread: {unread_books}\n")

# # 📝 Function to print details of one book
# def print_book(book):
#     print(f"\n📖 Title: {book['title']}")
#     print(f"✍ Author: {book['author']}")
#     print(f"📅 Year: {book['year']}")
#     print(f"📂 Genre: {book['genre']}")
#     print(f"📘 Read: {'✅ Yes' if book['read'] else '❌ No'}\n")

# # 🧭 Main function to show menu and handle user choices
# def main():
#     library = load_library()  # Load existing library data

#     # Keep showing the menu until user exits
#     while True:
#         print("\n📚 Main Menu")
#         print("1️⃣ Add a Book")
#         print("2️⃣ Remove a Book")
#         print("3️⃣ Search for a Book")
#         print("4️⃣ List All Books")
#         print("5️⃣ Mark Book as Read/Unread")
#         print("6️⃣ Show Statistics")
#         print("7️⃣ Exit")

#         # Ask user to choose an option
#         choice = input("\n➡ Enter your choice (1-7): ").strip()

#         # Run the function based on user's choice
#         if choice == "1":
#             add_book(library)
#         elif choice == "2":
#             remove_book(library)
#         elif choice == "3":
#             search_book(library)
#         elif choice == "4":
#             list_books(library)
#         elif choice == "5":
#             update_read_status(library)
#         elif choice == "6":
#             show_statistics(library)
#         elif choice == "7":
#             print("\n👋 Goodbye! Happy Reading!\n")
#             break
#         else:
#             print("\n⚠ Invalid choice! Please enter a number from 1 to 7.\n")

# # 🚀 Start the program from here
# if __name__ == "__main__":
#     main()
