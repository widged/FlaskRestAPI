# FOLLOW THIS INSTRUCTIONS AFTER THE GET_REQUEST.md

## POST / ADD BOOKS

## Note: Always restart your server after making a change

## Step 1

Ensure you have the following import statements

```python
# Importing flask and Json library
from flask import Flask, json, jsonify, request
```

## Note

`jsonify` and `request` allow you convert the response to a Json object and allows you to send a request respectively

## Step 2

Add a book with the function below

```python
# Adding a new book
@app.route('/books', methods=['POST'])
def add_book():
    # Getting the request object sent by the user
    return jsonify(request.get_json())

```

## Step 3

 Open Postman to test your function by using the route below
<http://localhost:5000/books>

## Note: The method to use in postman should be POST

## Step 4

Use this as a request body

```json
{
    "name": "Willy",
    "price": 23.4,
    "isbn": 123456788
}
```

Then Run the request by clicking the run button

## Validation

Validate the list of books json from the client by creating the function below

```python
# Validating request from the client

def validBookObject(bookObject):
    if("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

```

Then update the code from **step 2** into

```python

# Adding a new book

@app.route('/books', methods=['POST'])
def add_book():
    # Getting the request object sent by the user
    request_data = request.get_json()
    # Checking if the request is a valid book structure
    if(validBookObject(request_data)):
        # Inserting the valid book into the list of books
        books.insert(0, request_data)
        return "True"
    else:
        return "False"


```

## Step 5

Test the below route with a post request in postman
<http://localhost:5000/books>

It would return True if a valid Json request was sent, else, False

## Step 6

To further prevent the client from entering garbage key value in the json request, update the add_book function to

```python

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
        return "True"
    else:
        return "False"

```

## Step 7

In order to use the Response constructor, import the class by editing your import staement to look like the code below

```python
from flask import Flask, json, jsonify, request, Response
```

## Step 8

To send the right status code and response header, update your add_books function to the code below

```python

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
        return "False"
```

## Step 9

To show a proper error message to the client, update the else block in the add_book function to the code below

```python
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
```
