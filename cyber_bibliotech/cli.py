#!/usr/bin/env python3
"""Command-line interface for Cyber BiblioTech."""

import sys
from typing import Optional
from .library import Library
from .book import Book


class CLI:
    """Command-line interface for the digital library."""
    
    def __init__(self):
        """Initialize the CLI."""
        self.library = Library()
    
    def print_help(self):
        """Print help message."""
        print("""
Cyber BiblioTech - Digital Library for Tech Headz

Commands:
  add       Add a new book to the library
  list      List all books in the library
  search    Search for books
  remove    Remove a book by ISBN
  help      Show this help message
  quit      Exit the application

Usage:
  add <title> <author> <isbn> [year] [genre]
  list
  search <query>
  remove <isbn>
""")
    
    def add_book_interactive(self):
        """Add a book interactively."""
        print("\n=== Add New Book ===")
        title = input("Title: ").strip()
        if not title:
            print("Error: Title is required")
            return
        
        author = input("Author: ").strip()
        if not author:
            print("Error: Author is required")
            return
        
        isbn = input("ISBN: ").strip()
        if not isbn:
            print("Error: ISBN is required")
            return
        
        year_input = input("Year (optional): ").strip()
        year = int(year_input) if year_input.isdigit() else None
        
        genre = input("Genre (optional): ").strip() or None
        description = input("Description (optional): ").strip() or None
        
        book = Book(
            title=title,
            author=author,
            isbn=isbn,
            year=year,
            genre=genre,
            description=description
        )
        
        if self.library.add_book(book):
            print(f"\n✓ Book added successfully: {book}")
        else:
            print(f"\n✗ Error: A book with ISBN {isbn} already exists")
    
    def list_books(self):
        """List all books in the library."""
        books = self.library.list_all_books()
        
        if not books:
            print("\nLibrary is empty. Add some books to get started!")
            return
        
        print(f"\n=== Library Contents ({len(books)} books) ===")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
            if book.description:
                print(f"   Description: {book.description}")
    
    def search_books(self, query: str):
        """Search for books."""
        if not query:
            query = input("Search query: ").strip()
        
        if not query:
            print("Error: Search query is required")
            return
        
        results = self.library.search_books(query)
        
        if not results:
            print(f"\nNo books found matching '{query}'")
            return
        
        print(f"\n=== Search Results ({len(results)} books) ===")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book}")
            if book.description:
                print(f"   Description: {book.description}")
    
    def remove_book(self, isbn: str):
        """Remove a book by ISBN."""
        if not isbn:
            isbn = input("ISBN to remove: ").strip()
        
        if not isbn:
            print("Error: ISBN is required")
            return
        
        book = self.library.get_book_by_isbn(isbn)
        if not book:
            print(f"\n✗ No book found with ISBN {isbn}")
            return
        
        print(f"\nFound: {book}")
        confirm = input("Are you sure you want to remove this book? (y/n): ").strip().lower()
        
        if confirm == 'y':
            if self.library.remove_book(isbn):
                print("✓ Book removed successfully")
            else:
                print("✗ Error removing book")
        else:
            print("Cancelled")
    
    def run_interactive(self):
        """Run the CLI in interactive mode."""
        print("Welcome to Cyber BiblioTech - Digital Library for Tech Headz")
        print("Type 'help' for available commands")
        
        while True:
            try:
                command = input("\nbibliotech> ").strip().lower()
                
                if not command:
                    continue
                
                if command in ['quit', 'exit', 'q']:
                    print("Thanks for using Cyber BiblioTech!")
                    break
                elif command == 'help':
                    self.print_help()
                elif command == 'add':
                    self.add_book_interactive()
                elif command == 'list':
                    self.list_books()
                elif command.startswith('search'):
                    query = command[6:].strip() if len(command) > 6 else ""
                    self.search_books(query)
                elif command.startswith('remove'):
                    isbn = command[6:].strip() if len(command) > 6 else ""
                    self.remove_book(isbn)
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' for available commands")
            
            except KeyboardInterrupt:
                print("\n\nThanks for using Cyber BiblioTech!")
                break
            except Exception as e:
                print(f"Error: {e}")


def main():
    """Main entry point."""
    cli = CLI()
    cli.run_interactive()


if __name__ == "__main__":
    main()
