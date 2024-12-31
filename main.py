from flask import Flask, render_template, jsonify
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

# Models
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Item {self.name}>"

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "price": self.price,
            "description": self.description
        }

# Create Database
engine = create_engine("sqlite:///store.db")
if not database_exists(engine.url):
    create_database(engine.url)

with app.app_context():
    # db.drop_all()
    db.create_all()

# Database Status
print(f'DB is created: {database_exists(engine.url)}')
print(f'DB: {engine.url}')

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

@app.route('/create', methods=['POST'])
def create_item():
    item = Item(name="Book", code="1451", price=100, description="Amazing Book")

    db.session.add(item)
    db.session.commit()

    return 'Item created'

@app.route("/users")
def user_list():
    items = db.session.execute(db.select(Item).order_by(Item.id)).scalars()
    data = [item.json() for item in items]
    return jsonify(data)
