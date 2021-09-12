# FOLLOW THIS INSTRUCTIONS AFTER THE PATCH_REQUEST.md

## Setting up the database

## Step 1

Create a file called BookModel.py in the same directory as the app.py

## Step 2

Import the needed packages

```python

from flask import Flask
# Import sql alchemy
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

```

## Step 3

Install flask sqlalchemy

`pip3 install flask_sqlalchemy`

## Note

You can use `pip freeze` to know the packages you have installed on your machine
