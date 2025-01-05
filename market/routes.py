from flask import render_template, jsonify, request
from market import db, app
from market.models import Item, User


# Routes
@app.route('/')
def page_home():
    return render_template('index.html')

@app.route('/products')
def page_products():
    data = Item.query.all()
    return render_template('products.html', items=data)

@app.route('/item', methods=['POST', 'GET'])
def item():
    if request.method == 'POST':
        data = Item(name="Book", code="1451", price=100, description="Amazing Book")
        db.session.add(data)
        db.session.commit()
        return 'Item created'
    else:
        data = Item.query.all()
        return jsonify([i.to_json() for i in data])

@app.route("/user", methods=['POST', 'GET'])
def user():
    if request.method == "POST":
        data = User(username="admin", email="admin@gmail.com", password="admin", budget=100.0)
        db.session.add(data)
        db.session.commit()

        return "User created"
    else:
        data = User.query.all()
        return jsonify([user.to_json() for user in data])
