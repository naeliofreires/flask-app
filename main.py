from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# App
app = Flask(__name__)

# DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app) # initialize the app with the extension

# Routes
@app.route('/') 
def page_home():
    return render_template('index.html')

@app.route('/products')
def page_products():
    items = [
        { "id": 1, "name": "Celular", "code": "01456", "price": "1200" },
        { "id": 2, "name": "Notebook", "code": "02489", "price": "3500" },
        { "id": 2, "name": "Keyboard", "code": "024109", "price": "500" }
    ]
    return render_template('products.html', items=items)