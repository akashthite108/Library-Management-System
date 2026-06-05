import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
status TEXT
)
""")

conn.commit()

def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    cursor.execute(
        "INSERT INTO books(title, author, status) VALUES(?,?,?)",
        (title, author, "Available")
    )

    conn.commit()
    print("Book Added Successfully!")

def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if not books:
        print("No Books Found!")
        return

    print("\nLibrary Books")
    print("-" * 50)

    for book in books:
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Status: {book[3]}")
        print("-" * 50)

def issue_book():
    book_id = input("Enter Book ID: ")

    cursor.execute(
        "UPDATE books SET status='Issued' WHERE id=?",
        (book_id,)
    )

    conn.commit()
    print("Book Issued Successfully!")

def return_book():
    book_id = input("Enter Book ID: ")

    cursor.execute(
        "UPDATE books SET status='Available' WHERE id=?",
        (book_id,)
    )

    conn.commit()
    print("Book Returned Successfully!")

def delete_book():
    book_id = input("Enter Book ID: ")

    cursor.execute(
        "DELETE FROM books WHERE id=?",
        (book_id,)
    )

    conn.commit()
    print("Book Deleted Successfully!")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        conn.close()
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")