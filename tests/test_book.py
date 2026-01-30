"""Tests for Book model."""

import pytest
from cyber_bibliotech.book import Book


def test_book_creation():
    """Test creating a book with all fields."""
    book = Book(
        title="The Pragmatic Programmer",
        author="Andrew Hunt",
        isbn="978-0135957059",
        year=2019,
        genre="Programming",
        description="A classic guide to software development"
    )
    
    assert book.title == "The Pragmatic Programmer"
    assert book.author == "Andrew Hunt"
    assert book.isbn == "978-0135957059"
    assert book.year == 2019
    assert book.genre == "Programming"
    assert book.description == "A classic guide to software development"


def test_book_minimal_fields():
    """Test creating a book with only required fields."""
    book = Book(
        title="Clean Code",
        author="Robert C. Martin",
        isbn="978-0132350884"
    )
    
    assert book.title == "Clean Code"
    assert book.author == "Robert C. Martin"
    assert book.isbn == "978-0132350884"
    assert book.year is None
    assert book.genre is None
    assert book.description is None


def test_book_to_dict():
    """Test converting book to dictionary."""
    book = Book(
        title="Design Patterns",
        author="Gang of Four",
        isbn="978-0201633610",
        year=1994,
        genre="Software Engineering"
    )
    
    book_dict = book.to_dict()
    
    assert book_dict["title"] == "Design Patterns"
    assert book_dict["author"] == "Gang of Four"
    assert book_dict["isbn"] == "978-0201633610"
    assert book_dict["year"] == 1994
    assert book_dict["genre"] == "Software Engineering"


def test_book_from_dict():
    """Test creating book from dictionary."""
    book_dict = {
        "title": "Refactoring",
        "author": "Martin Fowler",
        "isbn": "978-0134757599",
        "year": 2018,
        "genre": "Programming",
        "description": "Improving the design of existing code"
    }
    
    book = Book.from_dict(book_dict)
    
    assert book.title == "Refactoring"
    assert book.author == "Martin Fowler"
    assert book.isbn == "978-0134757599"
    assert book.year == 2018
    assert book.genre == "Programming"
    assert book.description == "Improving the design of existing code"


def test_book_str_full():
    """Test string representation with all optional fields."""
    book = Book(
        title="The Art of Computer Programming",
        author="Donald Knuth",
        isbn="978-0201896831",
        year=1997,
        genre="Computer Science"
    )
    
    book_str = str(book)
    assert "The Art of Computer Programming" in book_str
    assert "Donald Knuth" in book_str
    assert "978-0201896831" in book_str
    assert "1997" in book_str
    assert "Computer Science" in book_str


def test_book_str_minimal():
    """Test string representation with minimal fields."""
    book = Book(
        title="Introduction to Algorithms",
        author="Cormen et al.",
        isbn="978-0262033848"
    )
    
    book_str = str(book)
    assert "Introduction to Algorithms" in book_str
    assert "Cormen et al." in book_str
    assert "978-0262033848" in book_str
