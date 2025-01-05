from market import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

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
