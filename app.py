from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.Person import Nutzer
from models.Order import Order
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:....@localhost/PythonTest"
db = SQLAlchemy(app)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))

    create_dttm = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    products = db.relationship("Product", secondary="orders")


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))

    users = db.relationship("User", secondary="orders")


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    dttm = db.Column(db.DateTime, default=datetime.datetime.now())

    user = db.relationship(User, backref=db.backref("orders", cascade="all, delete-orphan"))
    product = db.relationship(Product, backref=db.backref("orders", cascade="all, delete-orphan"))


association_table = db.Table('association', db.Model.metadata,
                             db.Column('left', db.Integer, db.ForeignKey('A.id')),
                             db.Column('right', db.Integer, db.ForeignKey('B.id')))


class A(db.Model):
    __tablename__ = 'A'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    children = db.relationship("B", secondary=association_table)


class B(db.Model):
    __tablename__ = 'B'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


@app.route('/new/')
def foo():
    db.drop_all()
    db.create_all()
    a = A(name="start")
    b = B(name="end")
    a.children.append(b)
    db.session.add(a)
    db.session.commit()

    return "ok"


@app.route('/email=<string:email>/product=<string:product>')
def hello_world(product, email):
    db.drop_all()
    db.create_all()
    user1 = User(email=email)
    db.session.add(user1)
    db.session.commit()
    product1 = Product(title=product)
    db.session.add(product1)
    db.session.commit()

    order1 = Order(user=user1, product=product1)

    db.session.add(order1)
    db.session.commit()

    return 'Ok'


if __name__ == '__main__':
    app.run(debug=True)

