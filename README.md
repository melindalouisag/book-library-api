# Book Library Borrowing API

A simple RESTful API built with **Python** and **Flask** to manage a small book library and basic borrowing/returning of books.

The API starts with two sample books:

1. *The Picture of Dorian Gray* – Oscar Wilde  
2. *Babel* – R. F. Kuang  

All data is stored in memory (a Python list), which is enough for learning and for this assignment.

---

## 1. Project Description

This API allows you to:

- View all books in the library
- View a single book by ID
- Add a new book
- Update an existing book (title/author)
- Delete a book
- Borrow a book (mark it as unavailable and assign a borrower)
- Return a book (mark it as available again)

---

## 2. Technology Stack

- Python 3
- Flask 3.x

---

## 3. How to Run Locally

### Prerequisites

- Python 3 installed
- Git installed

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/melindalouisag/book-library-api.git
cd book-library-api

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python3 app.py
