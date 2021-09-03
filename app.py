# Importing flask
from flask import Flask

app = Flask(__name__)
print(__name__)

# Using a route decorator
@app.route('/')
def hello_world():
    return "Hello World!"

# Starting the server for the application on port 5000
app.run(port=5000)