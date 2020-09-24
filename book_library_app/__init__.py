from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

results = db.session.execute('show databases')
for row in results:
    print(row)

from book_library_app import authors
