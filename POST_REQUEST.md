# FOLLOW THIS INSTRUCTIONS AFTER THE GET_REQUEST.md

## POST / ADD BOOKS

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
