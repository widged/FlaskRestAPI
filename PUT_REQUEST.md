# FOLLOW THIS INSTRUCTIONS AFTER THE POST_REQUEST.md

## PUT / UPDATE BOOKS

## Note: Always restart your server after making a change

## Note 2: PUT method is used to make a change on all of the keys on the request sent by the client

## Step 1

Use this function to prevent clients from sending wrong requests.

```python

# function to validate the request from a client in order to accept just two of the requests
def valid_put_request_data(request_data):
    if('name' in request_data and 'price' in request_data):
        return True
    else:
        return False

```

## Step 2

Use the function below to create a PUT method

```python
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
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json')
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
```
