from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy_utils import database_exists, create_database

# Initialize Flask App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"

# Database Base Class
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create Database
engine = create_engine("sqlite:///store.db")
if not database_exists(engine.url):
    create_database(engine.url)

# Models
from market.models import User, Item

# Create Tables
with app.app_context():
    db.create_all()

# Database Status
print(f'DB is created: {database_exists(engine.url)}')
print(f'DB: {engine.url}')

# Initialize Routes
from market import routes