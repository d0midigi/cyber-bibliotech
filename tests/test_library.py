"""Tests for Library class."""

import pytest
import tempfile
import os
from pathlib import Path
from cyber_bibliotech.library import Library
from cyber_bibliotech.book import Book


@pytest.fixture
def temp_library():
    """Create a temporary library for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    library = Library(storage_file=temp_file)
    yield library
    
    # Cleanup
    if os.path.exists(temp_file):
        os.remove(temp_file)


def test_library_creation(temp_library):
    """Test creating a new library."""
    assert len(temp_library) == 0
    assert temp_library.list_all_books() == []


def test_add_book(temp_library):
    """Test adding a book to the library."""
    book = Book(
        title="Python Crash Course",
        author="Eric Matthes",
        isbn="978-1593279288"
    )
    
    result = temp_library.add_book(book)
    assert result is True
    assert len(temp_library) == 1
    assert temp_library.list_all_books()[0] == book


def test_add_duplicate_isbn(temp_library):
    """Test that duplicate ISBNs are not allowed."""
    book1 = Book(
        title="Book One",
        author="Author One",
        isbn="123-456-789"
    )
    book2 = Book(
        title="Book Two",
        author="Author Two",
        isbn="123-456-789"  # Same ISBN
    )
    
    assert temp_library.add_book(book1) is True
    assert temp_library.add_book(book2) is False
    assert len(temp_library) == 1


def test_remove_book(temp_library):
    """Test removing a book from the library."""
    book = Book(
        title="Test Book",
        author="Test Author",
        isbn="111-222-333"
    )
    
    temp_library.add_book(book)
    assert len(temp_library) == 1
    
    result = temp_library.remove_book("111-222-333")
    assert result is True
    assert len(temp_library) == 0


def test_remove_nonexistent_book(temp_library):
    """Test removing a book that doesn't exist."""
    result = temp_library.remove_book("999-999-999")
    assert result is False


def test_search_books_by_title(temp_library):
    """Test searching books by title."""
    book1 = Book(title="Python Programming", author="Author A", isbn="111")
    book2 = Book(title="Java Programming", author="Author B", isbn="222")
    book3 = Book(title="Python for Data Science", author="Author C", isbn="333")
    
    temp_library.add_book(book1)
    temp_library.add_book(book2)
    temp_library.add_book(book3)
    
    results = temp_library.search_books("Python")
    assert len(results) == 2
    assert book1 in results
    assert book3 in results


def test_search_books_by_author(temp_library):
    """Test searching books by author."""
    book1 = Book(title="Book A", author="John Smith", isbn="111")
    book2 = Book(title="Book B", author="Jane Doe", isbn="222")
    book3 = Book(title="Book C", author="John Doe", isbn="333")
    
    temp_library.add_book(book1)
    temp_library.add_book(book2)
    temp_library.add_book(book3)
    
    results = temp_library.search_books("John")
    assert len(results) == 2
    assert book1 in results
    assert book3 in results


def test_search_books_case_insensitive(temp_library):
    """Test that search is case-insensitive."""
    book = Book(title="Clean Code", author="Robert Martin", isbn="123")
    temp_library.add_book(book)
    
    results = temp_library.search_books("CLEAN")
    assert len(results) == 1
    assert book in results


def test_search_no_results(temp_library):
    """Test searching when no results match."""
    book = Book(title="Test Book", author="Test Author", isbn="123")
    temp_library.add_book(book)
    
    results = temp_library.search_books("nonexistent")
    assert len(results) == 0


def test_get_book_by_isbn(temp_library):
    """Test getting a book by ISBN."""
    book = Book(title="Test", author="Author", isbn="123-456")
    temp_library.add_book(book)
    
    found_book = temp_library.get_book_by_isbn("123-456")
    assert found_book == book


def test_get_book_by_isbn_not_found(temp_library):
    """Test getting a book by ISBN when it doesn't exist."""
    found_book = temp_library.get_book_by_isbn("999-999")
    assert found_book is None


def test_save_and_load(temp_library):
    """Test saving and loading library data."""
    book1 = Book(title="Book 1", author="Author 1", isbn="111", year=2020)
    book2 = Book(title="Book 2", author="Author 2", isbn="222", genre="Fiction")
    
    temp_library.add_book(book1)
    temp_library.add_book(book2)
    
    # Create a new library instance with the same storage file
    storage_file = temp_library.storage_file
    new_library = Library(storage_file=str(storage_file))
    
    assert len(new_library) == 2
    books = new_library.list_all_books()
    
    # Check that books were loaded correctly
    assert any(b.isbn == "111" and b.title == "Book 1" for b in books)
    assert any(b.isbn == "222" and b.title == "Book 2" for b in books)


def test_list_all_books(temp_library):
    """Test listing all books."""
    book1 = Book(title="Book 1", author="Author 1", isbn="111")
    book2 = Book(title="Book 2", author="Author 2", isbn="222")
    
    temp_library.add_book(book1)
    temp_library.add_book(book2)
    
    all_books = temp_library.list_all_books()
    assert len(all_books) == 2
    assert book1 in all_books
    assert book2 in all_books
