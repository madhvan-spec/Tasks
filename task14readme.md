# Library Management System

This is a Python-based Library Management System that allows members to borrow and return books, and admins to manage books, libraries, and book copies. The system persists data in a JSON file, ensuring that all information is saved and loaded across sessions.

## Features

### Admin Features
- Add new books with title, author, and genre
- Add new libraries
- Add copies of existing books to libraries
- View the raw JSON data file
- Logout from admin menu

### Member Features
- Register as a new member or login as an existing member
- **Borrow books:**
  - A member can borrow only one copy of a specific book at a time
  - A member can borrow multiple different books simultaneously
- Return borrowed books
- View a list of currently borrowed books
- Logout from member menu

## Data Persistence

- All books, members, libraries, book copies, and counters are stored in a JSON file named `task14.json`
- On program start, the system loads all existing data
- After any action (borrow, return, add book, add copy), the data is automatically saved

## Classes Overview

### 1. Book
Represents a book.

**Attributes:**
- `book_id` - Unique identifier
- `title` - Book title
- `author` - Author name
- `genre` - Book genre

**Methods:**
- `get_book_details()` – Print details of the book
- `to_json()` / `from_json()` – For saving/loading JSON data

### 2. BookCopy
Represents a copy of a book in a library.

**Attributes:**
- `copy_id` - Unique identifier for the copy
- `book_id` - Reference to the book
- `library_id` - Which library the copy belongs to
- `is_available` - Boolean indicating availability
- `borrowed_by` - Member ID if borrowed, None if available

**Methods:**
- `to_json()` / `from_json()` – For saving/loading JSON data

### 3. Member
Represents a library member.

**Attributes:**
- `member_id` - Unique identifier
- `name` - Member name
- `library_id` - Home library
- `borrowed_copies` - List of borrowed copy IDs

**Methods:**
- `to_json()` / `from_json()` – For saving/loading JSON data

### 4. Library
Represents a library.

**Attributes:**
- `library_id` - Unique identifier
- `name` - Library name
- `books` - Dictionary of books in the library
- `copies` - Dictionary of book copies in the library
- `members` - Dictionary of registered members

**Methods:**
- `to_json()` / `from_json()` – For saving/loading JSON data

### 5. LibrarySystem
Central system that manages all books, libraries, members, and book copies.

**Key Methods:**
- `save_data()` – Save all system data to `task14.json`
- `load_data()` – Load all data from `task14.json`
- `add_books()`, `add_library()`, `add_book_copy()` – Admin functions
- `member_login_or_register()` – Login or register members
- `borrow_book(library, member)` – Borrow a book copy

## File Structure

```
task14.py           - Main implementation
task14.json         - Data persistence file (auto-generated)
task14readme.md     - This file
```

## Getting Started

1. Run `task14.py` to start the Library Management System
2. Choose between Admin or Member login
3. Follow the menu prompts to interact with the system

## Data Format

All data is persisted in `task14.json` with the following structure:
- `books` - Collection of all books
- `members` - Collection of all registered members
- `book_copies` - Collection of all book copies
- `libraries` - Collection of all libraries
- `counters` - ID counters for generating unique identifiers
