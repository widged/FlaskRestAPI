# FOLLOW THIS INSTRUCTIONS AFTER THE README

## GET

### Note: The default method of all endpoint is a get method

`# Importing flask  and Json library`

`from flask import Flask, jsonify`

`app = Flask(__name__)`

`# Creating a list of books`
`books = [`
    `# Adding dictionaries to hold the some book details`
    `{
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 987654321,
    },`  

    {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 123456789,

    }
    ]
`# Route to get all books`
`@app.route('/books')`

`def getAllBooks():`

        return jsonify({'books' : books})

`# Starting the server for the application on port 5000`

`app.run(port=5000)`

## NOTE: Always restart your server after adding a new route or making an update

## Step

To view the output on the browser, visit <http://localhost:5000/books>
