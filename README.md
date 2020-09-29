## About

The project is a Python/Flask REST API for book library app back-end. It supports user, author and book resources, and also includes authentication through JWT.

## Features

The application provides features of **registering new users, logging in, updating and fetching users**, as well as **listing, adding, updating and removing** books and authors. To simplify the database relations, it is assumed that the book can have only one author.

Detailed lsit of available endpoints, accepted parameters and request body format is available in the [documentation](https://documenter.getpostman.com/view/5659673/TVKJyuyi).

## Documentation

The Postman documentation is available online at [https://documenter.getpostman.com/view/5659673/TVKJyuyi](https://documenter.getpostman.com/view/5659673/TVKJyuyi). There is also a HTML version of the documentiation in `documentation.html` file in the main project folder.

## Setup

- Clone repository
- Create database and user
- Set up the .env file (instructions below)
- Create virtual environment:
```
python -m venv venv
```
- Install packages from `requirements.txt`:
```
pip install -r requirements.txt
```
- Migrate database:
```
flask db upgrade
```
- Enter "Run" command:
```
flask run
```

The .env file should be in the following format:
```
SECRET_KEY=EnterYourSecretKeyHere
SQLALCHEMY_DATABASE_URI=EnterYourSqlAlchemyUriHere
```
You can rename .env.example file and set your values as in the example above.

## Populating the DB with sample data
To populate the database with pre-made data use `flask db-manage add-data` command. To remove remove all data, enter `flask db-manage remove-data`.

## Tests
To execute the tests located in `tests/` enter the command:
```
python -m pytest tests/
```

## Technologies

Technology-wise, the app utilizes:
- Python 3.8.6
- Flask 1.1.2
- Alembic 1.4.3
- SQLAlchemy 1.3.19
- Pytest 6.1.0
- MySQL database
- SQLite for testing purposes
- Postman
