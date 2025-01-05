from flask import render_template, jsonify
from market import db, app
from market.models import Item


# Routes
@app.route('/')
def page_home():
    return render_template('index.html')

@app.route('/products')
def page_products():
    # items = [
    #     { "id": 1, "name": "Celular", "code": "01456", "price": "1200" },
    #     { "id": 2, "name": "Notebook", "code": "02489", "price": "3500" },
    #     { "id": 2, "name": "Keyboard", "code": "024109", "price": "500" }
    # ]
    data = Item.query.all();
    return render_template('products.html', items=data)

@app.route('/create', methods=['POST'])
def create_item():
    item = Item(name="Book", code="1451", price=100, description="Amazing Book")

    db.session.add(item)
    db.session.commit()

    return 'Item created'

@app.route("/users")
def user_list():
    items = db.session.execute(db.select(Item).order_by(Item.id)).scalars()
    data = [item.to_json() for item in items]
    return jsonify(data)
