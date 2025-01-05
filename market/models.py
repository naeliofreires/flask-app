from market import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Float, nullable=False, default=1000)
    items = db.relationship('Item', backref='owner_user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "budget": self.budget
        }


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Item {self.name}>"

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "price": self.price,
            "description": self.description
        }