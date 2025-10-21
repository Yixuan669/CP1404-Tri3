"""
CP1404 Assignment 1 - Books to Read
Name:Zhang Yixuan
Date Started: 21/10/2025
GitHub URL:
"""

import csv
FILENAME = "books.csv"

MENU = ("""
Menu: 
D - Display books 
A - Add a new book 
C - Complete a book 
Q - Quit""" )

def main():
    """..."""
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>>").upper()
        if choice == "D":
            print_books_information(FILENAME)
        elif choice == "Q":
            print("So many books, so little time. Frank Zappa")
        else:
            print("Invalid menu choice ")

def print_books_information(FILENAME):
    total_pages_left = 0
    unread_books = 0
    books_to_author = {}
    i = 1
    with open(FILENAME) as in_file:
        reader = list(csv.reader(in_file))
        maximum_title_length = max(len(record[0]) for record in reader)
        maximum_author_length = max(len(record[1]) for record in reader)
        maximum_pages_length = max(len(record[2]) for record in reader)
        for record in reader:
            book_name = record[0]
            author_name = record[1]
            page_number = int(record[2])
            book_status = record[3]
            if book_status == "u":
                mark = "*"
                total_pages_left += page_number
                unread_books += 1
            else:
                mark = " "
            print(f'{mark}{i}.{book_name:{maximum_title_length}} by {author_name:{maximum_author_length}} {page_number:>{maximum_pages_length}} pages')
            i += 1
    print(f"You still need to read {total_pages_left} pages in {unread_books} books.")
    return books_to_author

main()