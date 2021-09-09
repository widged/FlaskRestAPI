# FOLLOW THIS INSTRUCTIONS AFTER THE PUT_REQUEST.md

## PATCH / UPDATE BOOKS

## Note: Always restart your server after making a change

## Delete a book using the function and route below

```python

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
```
