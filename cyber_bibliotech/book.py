"""Book model for the digital library."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Book:
    """Represents a book in the digital library."""
    
    title: str
    author: str
    isbn: str
    year: Optional[int] = None
    genre: Optional[str] = None
    description: Optional[str] = None
    
    def to_dict(self):
        """Convert book to dictionary."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        """Create book from dictionary."""
        return cls(**data)
    
    def __str__(self):
        """String representation of the book."""
        year_str = f" ({self.year})" if self.year else ""
        genre_str = f" [{self.genre}]" if self.genre else ""
        return f"{self.title} by {self.author}{year_str}{genre_str} - ISBN: {self.isbn}"
