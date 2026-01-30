"""Library class for managing book collections."""

import json
from pathlib import Path
from typing import List, Optional
from .book import Book


class Library:
    """Digital library for managing books."""
    
    def __init__(self, storage_file: str = "library_data.json"):
        """Initialize the library.
        
        Args:
            storage_file: Path to JSON file for storing library data
        """
        self.storage_file = Path(storage_file)
        self.books: List[Book] = []
        self.load()
    
    def add_book(self, book: Book) -> bool:
        """Add a book to the library.
        
        Args:
            book: Book object to add
            
        Returns:
            True if book was added, False if ISBN already exists
        """
        # Check for duplicate ISBN
        if any(b.isbn == book.isbn for b in self.books):
            return False
        
        self.books.append(book)
        self.save()
        return True
    
    def remove_book(self, isbn: str) -> bool:
        """Remove a book from the library by ISBN.
        
        Args:
            isbn: ISBN of the book to remove
            
        Returns:
            True if book was removed, False if not found
        """
        initial_count = len(self.books)
        self.books = [b for b in self.books if b.isbn != isbn]
        
        if len(self.books) < initial_count:
            self.save()
            return True
        return False
    
    def search_books(self, query: str) -> List[Book]:
        """Search for books by title, author, or ISBN.
        
        Args:
            query: Search query string
            
        Returns:
            List of matching books
        """
        query_lower = query.lower()
        return [
            book for book in self.books
            if query_lower in book.title.lower()
            or query_lower in book.author.lower()
            or query_lower in book.isbn.lower()
        ]
    
    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """Get a book by its ISBN.
        
        Args:
            isbn: ISBN to search for
            
        Returns:
            Book if found, None otherwise
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def list_all_books(self) -> List[Book]:
        """Get all books in the library.
        
        Returns:
            List of all books
        """
        return self.books.copy()
    
    def save(self):
        """Save library data to JSON file using atomic write."""
        data = {
            "books": [book.to_dict() for book in self.books]
        }
        # Use atomic write: write to temp file, then rename
        storage_path = Path(self.storage_file)
        temp_file = storage_path.with_suffix('.tmp')
        try:
            with open(temp_file, 'w') as f:
                json.dump(data, f, indent=2)
            # Atomic rename on POSIX systems
            temp_file.replace(storage_path)
        except Exception:
            # Clean up temp file if something went wrong
            if temp_file.exists():
                temp_file.unlink()
            raise
    
    def load(self):
        """Load library data from JSON file."""
        if not self.storage_file.exists():
            return
        
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                self.books = [Book.from_dict(book_data) for book_data in data.get("books", [])]
        except (json.JSONDecodeError, TypeError, ValueError):
            # If file is corrupted or has invalid data, start fresh
            self.books = []
    
    def __len__(self):
        """Return the number of books in the library."""
        return len(self.books)
