from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" of books
books = [
    {
        "id": 1,
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "available": True,
        "borrower": None
    },
    {
        "id": 2,
        "title": "Babel",
        "author": "R. F. Kuang",
        "available": True,
        "borrower": None
    }
]


def find_book(book_id: int):
    """Helper function to find a book by id."""
    for book in books:
        if book["id"] == book_id:
            return book
    return None


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Welcome to the Book Library Borrowing API",
            "endpoints": [
                "GET    /books",
                "GET    /books/<id>",
                "POST   /books",
                "PUT    /books/<id>",
                "DELETE /books/<id>",
                "POST   /books/<id>/borrow",
                "POST   /books/<id>/return",
            ],
        }
    )


# 1. GET /books - retrieve all books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200


# 2. GET /books/<id> - retrieve a single book
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = find_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200


# 3. POST /books - add a new book
@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()

    if not data or "title" not in data or "author" not in data:
        return jsonify({"error": "title and author are required"}), 400

    new_id = max((book["id"] for book in books), default=0) + 1

    new_book = {
        "id": new_id,
        "title": data["title"],
        "author": data["author"],
        "available": True,
        "borrower": None,
    }

    books.append(new_book)
    return jsonify(new_book), 201


# 4. PUT /books/<id> - update book info (title/author)
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = find_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json() or {}

    title = data.get("title")
    author = data.get("author")

    if title:
        book["title"] = title
    if author:
        book["author"] = author

    return jsonify(book), 200


# 5. DELETE /books/<id> - delete a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = find_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    books.remove(book)
    return jsonify({"message": "Book deleted"}), 200


# 6. POST /books/<id>/borrow - borrow a book
@app.route("/books/<int:book_id>/borrow", methods=["POST"])
def borrow_book(book_id):
    book = find_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    if not book["available"]:
        return jsonify({"error": "Book is already borrowed"}), 400

    data = request.get_json() or {}
    borrower = data.get("borrower")

    if not borrower:
        return jsonify({"error": "borrower field is required"}), 400

    book["available"] = False
    book["borrower"] = borrower

    return jsonify(book), 200


# 7. POST /books/<id>/return - return a book
@app.route("/books/<int:book_id>/return", methods=["POST"])
def return_book(book_id):
    book = find_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    if book["available"]:
        return jsonify({"error": "Book is not currently borrowed"}), 400

    book["available"] = True
    book["borrower"] = None

    return jsonify(book), 200


if __name__ == "__main__":
    print("Starting Flask server...")  # so you SEE output
    app.run(debug=True)
