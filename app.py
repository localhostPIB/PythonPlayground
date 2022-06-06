from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.Person import Nutzer
from models.Order import Order

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:OliverRoot@localhost/PythonTest"
db = SQLAlchemy(app)


@app.route('/', methods=["GET"])
def hello_world():
    db.drop_all()
    db.create_all()
    order = Order(name="CD")
    db.session.add(order)
    db.session.commit()
    n = Nutzer(username="Flask", email="example@example.com")
    nutzerList = db.session.query(Nutzer).filter_by(username=n.username).all()

    if not nutzerList:
        db.session.add(n)
        db.session.commit()
        return "new inn ;-)"

    return 'Hello World!'


@app.route('/user/<string:name>', methods=["GET"])
def newUser(name):
    n = Nutzer(username=name, email=name + "@example.com")
    db.session.add(n)
    db.session.commit()
    return jsonify(n.to_json())


@app.route('/search/all', methods=["GET"])
def getAllUser():
    result = db.session.query(Nutzer).all()

    return jsonify([nutzer.to_json() for nutzer in result])


@app.route('/search/p=<string:name>', methods=["GET"])
def searchUserByUsername(name):
    result = db.session.query(Nutzer).filter_by(username=name)

    return jsonify([nutzer.to_json() for nutzer in result])


@app.route('/search/email=<string:email>', methods=["GET"])
def searchUserByEmail(email):
    result = db.session.query(Nutzer).filter_by(email=email)

    return jsonify([nutzer.to_json() for nutzer in result])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
