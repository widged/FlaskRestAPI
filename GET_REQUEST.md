# FOLLOW THIS INSTRUCTIONS AFTER THE README

## GET ALL BOOKS

### Note: The default method of all endpoint is a get method

```python
# Importing flask  and Json library

from flask import Flask, jsonify

app = Flask(__name__)

# Creating a list of books
books = [
    # Adding dictionaries to hold the some book details
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 987654321,
    },  

    {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 123456789,

    }
    ]
# Route to get all books
@app.route('/books')

def getAllBooks():

        return jsonify({'books' : books})

# Starting the server for the application on port 5000

app.run(port=5000)

```

## NOTE: Always restart your server after adding a new route or making an update

## Step1

To view the output on the browser, visit <http://localhost:5000/books>

## GET A SINGLE BOOK

### Use the functino below to get a single book by ISBN

```python
# Route to get book by isbn


@app.route('/book/<int:isbn>')
def getBookByISBN(isbn):
    # Empty dictionary to hold the found book
    return_value = {}
    # Looping through the dictionary of books
    for book in books:
        # If the book is found, populate the initial empty dictionary with the found values
        if(book['isbn'] == isbn):
            return_value = {
                'name': book['name'],
                'price': book['price'],
            }
            # Returning a json of the found book isbn
    return jsonify(return_value)
```

## Step2

To view the output on the browser, visit <http://localhost:5000/book/{isbn_number}>
eg
<http://localhost:5000/book/123456789>
