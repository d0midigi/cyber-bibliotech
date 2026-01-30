# Cyber BiblioTech 📚

A Cyber BiblioTech for Tech Headz - A digital library management system for managing your technical book collection.

## Features

- **Add Books**: Add books to your library with title, author, ISBN, year, genre, and description
- **List Books**: View all books in your collection
- **Search Books**: Search by title, author, or ISBN
- **Remove Books**: Remove books from your library by ISBN
- **Persistent Storage**: All data is saved to JSON for persistence between sessions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/d0midigi/cyber-bibliotech.git
cd cyber-bibliotech
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Run the application in interactive mode:

```bash
python bibliotech.py
```

This will launch an interactive shell where you can use the following commands:

- `add` - Add a new book to the library
- `list` - List all books in the library
- `search <query>` - Search for books
- `remove <isbn>` - Remove a book by ISBN
- `help` - Show available commands
- `quit` - Exit the application

### Example Session

```
Welcome to Cyber BiblioTech - Digital Library for Tech Headz
Type 'help' for available commands

bibliotech> add

=== Add New Book ===
Title: The Pragmatic Programmer
Author: Andrew Hunt
ISBN: 978-0135957059
Year (optional): 2019
Genre (optional): Programming
Description (optional): A classic guide to software development

✓ Book added successfully: The Pragmatic Programmer by Andrew Hunt (2019) [Programming] - ISBN: 978-0135957059

bibliotech> list

=== Library Contents (1 books) ===
1. The Pragmatic Programmer by Andrew Hunt (2019) [Programming] - ISBN: 978-0135957059
   Description: A classic guide to software development

bibliotech> search pragmatic

=== Search Results (1 books) ===
1. The Pragmatic Programmer by Andrew Hunt (2019) [Programming] - ISBN: 978-0135957059
   Description: A classic guide to software development

bibliotech> quit
Thanks for using Cyber BiblioTech!
```

## Development

### Running Tests

Run the test suite:

```bash
pytest tests/ -v
```

### Project Structure

```
cyber-bibliotech/
├── cyber_bibliotech/
│   ├── __init__.py
│   ├── book.py          # Book model
│   ├── library.py       # Library management
│   └── cli.py           # Command-line interface
├── tests/
│   ├── test_book.py     # Book model tests
│   └── test_library.py  # Library tests
├── bibliotech.py        # Main entry point
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Data Storage

Library data is stored in `library_data.json` in the current directory. This file is automatically created when you add your first book.

## License

MIT License - Feel free to use and modify as needed!
