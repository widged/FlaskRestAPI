# FOLLOW THIS INSTRUCTIONS AFTER THE PUT_REQUEST.md

## PATCH / UPDATE BOOKS

## Note: Always restart your server after making a change

## Note 2: PATCH method only requires the key of the json to be changed and not all the key's and values like PUT

## Use the function to get a PUT request

```python
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

```
