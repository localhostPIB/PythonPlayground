import uuid
from . import db
from sqlalchemy.dialects.postgresql import UUID


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String, nullable=False)

    users = db.relationship("Person", secondary="orders")

    def to_json(self):
        return {
            'id ': self.id,
            'name ': self.name
        }


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    products = db.relationship("Product", secondary="orders")

    def to_json(self):
        return {
            'id ': self.id,
            'username ': self.username,
            'email ': self.email
        }


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    person_id = db.Column(UUID(as_uuid=True), db.ForeignKey('persons.id'))
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey('products.id'))

    user = db.relationship("Person", backref=db.backref("orders", cascade="all, ""delete-orphan"))
    product = db.relationship("Product", backref=db.backref("orders", cascade="all, delete-orphan"))

    def to_json(self):
        return {
            'id ': self.id
        }
