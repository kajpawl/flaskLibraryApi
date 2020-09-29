## About

The project is a Python/Flask REST API for book library app back-end. It supports user, author and book resources.

## Features

The application provides features of **registering new users, logging in, updating and fetching users**, as well as **listing, adding, updating and removing** books and authors. To simplify the database relations, it is assumed that the book can have only one author.

Detailed lsit of available endpoints, accepted parameters and request body format is available in the [documentation](https://documenter.getpostman.com/view/5659673/TVKJyuyi).

## Technologies

Technology-wise, the app utilizes:
- Python
- Flask framework
- Flask-Migrate, Flask-SQLAlchemy, Marshmallow libraries
- MySQL database
- PyTest and SQLite - for testing purposes.

## Documentation

The Postman documentation is available online at [https://documenter.getpostman.com/view/5659673/TVKJyuyi](https://documenter.getpostman.com/view/5659673/TVKJyuyi). There is also a HTML version of the documentiation in `documentation.html` file in the main project folder.

## Steps to run

To run the app simply enter `flask run` in the terminal. To populate the database with pre-made data use `flask db-manage add-data` command. To remove remove all data, enter `flask db-manage remove-data`.
