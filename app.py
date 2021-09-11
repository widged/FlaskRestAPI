# Importing flask and Json library
from logging import error
from os import stat
from flask import Flask, json, jsonify, request, Response
from settings import *

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

# Using a route decorator


@app.route('/')
def hello_world():
    return "Hello World!"

# Route to get all books


@app.route('/books')
def getAllBooks():
    return jsonify({'books': books})

# Route to get book by isbn


@app.route('/book/<int:isbn>')
def getBookByISBN(isbn):
    # Empty dictionary to hold the found book
    return_value = {}
    # Looping through the dictionary of books
    for book in books:
        # If the book is found, populate the initial empty dictionary with the found values
        if(book['isbn'] == isbn):
            # Response if isbn is found
            return_value = {
                'name': book['name'],
                'price': book['price']
            }
        else:
            # Response if isbn isn't found
            return_value = {
                'error': 'ISBN not found'
            }

            # Returning a json of the book by isbn
    return jsonify(return_value)

# Validating request from the client


def validBookObject(bookObject):
    if("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

# Adding a new book


@app.route('/books', methods=['POST'])
def add_book():
    # Getting the request object sent by the user
    request_data = request.get_json()
    # Checking if the request is a valid book structure
    if(validBookObject(request_data)):
        # Further checking and accepting only the needed keys from the clients request
        new_book = {
            'name': request_data['name'],
            'price': request_data['price'],
            'isbn': request_data['isbn']
        }
        # Inserting the valid book into the list of books
        books.insert(0, new_book)
        # Having the response constructor to send the right status code and header location
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        # Returning an invalid book error response
        invalidBookObjectErrorMsg = {
            "error": "Invalid book passed in the request",
            "helpString": "Pass data similar to this {'name':'The Cat Runs','price': 3.45,'isbn':234567890}"
        }
        # Returning the response to the client
        response = Response(json.dumps(invalidBookObjectErrorMsg),
                            status=400, mimetype="application/json")
        return response
# NOTE: USE json.dumps() method to convert python dictionaires to json objects

# function to validate the request from a client in order to accept just two of the requests


def valid_put_request_data(request_data):
    if('name' in request_data and 'price' in request_data):
        return True
    else:
        return False

# function to replace a particular book and all of its data


@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    # Handling wrong request error
    if(not valid_put_request_data(request_data)):
        invalidBookObjectErrorMsg = {
            "error": "Invalid book passed in the request",
            "helpString": "Pass data similar to this {'name':'The Cat Runs','price': 3.45,'isbn':234567890}"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg),
                            status=400, mimetype='application/json')
        return response

    new_book = {
        'name': request_data['name'],
        'price': request_data['price'],
        'isbn': isbn
    }

    # Counter to check throgugh each dictionary of books
    i = 0
    # Iterating through the list of books
    for book in books:
        # Getting the isbn of each iteration
        currentISBN = book['isbn']
        # Checking if the isbn entered matches any isbn in the dictionary of books
        if currentISBN == isbn:
            # Replacing the books data with the new_book data
            books[i] = new_book
        # Increasing the counter to the next ISBN if the entered ISBN doesn't exist in the first ISBN in the dictionary
        i += 1
        # Response if the book was found and replaced
    response = Response("", status=204)
    return response

# Creating a patch function
@app.route('/books/<int:isbn>', methods=['PATCH'])
def updateBook(isbn):
    
    # Getting the request data
    request_data = request.get_json()

# Create an empty dictionary to hold the new data
    updated_book = {}
    # Checking if the name key is in the json request from the clinet
    if('name' in request_data):
        # Setting the key and value of the updated_book dictionary to the new value
        updated_book['name'] = request_data['name']
    if('price' in request_data):
        # Setting the key and value of the updated_book dictionary to the new value
        updated_book['price'] = request_data['price']
    # Looping through the books to find if an isbn is matched with the clients request
    for book in books:
        if book['isbn'] == isbn:
            # Updating the book dictionary to reflect the change on the updated_book dictionary
            book.update(updated_book)
    response = Response("", status=204)
    # Setting the location to reflect a link on how to get the newly updated book
    response.headers['Location'] = "/books/" + str(isbn)

    return response

# Deleting a book based on a clients request
@app.route('/books/<int:isbn>',  methods=['DELETE'])

def delete_book(isbn):
    # Create a counter to check the iteration of each books
    i = 0
    for book in books:
        # Checking if the book exists in the dictionary
        if(book['isbn'] == isbn):
            # Deleting the book using the index number
            books.pop(i)
            response = Response("", status=204)
            return response
        # Increasing the loop for each iteration
        i += 1
    # Response if the isbn wasn't found
    error_message = {'error': 'The book with that ISBN was not found.'}
    response = Response(json.dumps(error_message), status=404, mimetype='application/json')
    return response

# Used to show error messages
if __name__ == "__main__":
      app.run(debug=True)

# Starting the server for the application on port 5000
app.run(port=5000)
