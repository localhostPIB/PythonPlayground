from flask import jsonify
from models import db, create_app
from models.models import Person, Product, Order

app = create_app()


@app.route('/', methods=["GET"])
def hello_world():
    db.drop_all()
    db.create_all()
    order = Order()

    n = Person(username="Flask", email="example@example.com")
    nutzerList = db.session.query(Person).filter_by(username=n.username).all()

    if not nutzerList:
        db.session.add(n)
        db.session.commit()

    product1 = Product(name="CD")
    order.product = product1
    order.user = n
    db.session.add(order)
    db.session.commit()

    return "new inn ;-)"


@app.route('/user/<string:name>', methods=["GET"])
def newUser(name):
    n = Person(username=name, email=name + "@example.com")
    db.session.add(n)
    db.session.commit()
    return jsonify(n.to_json())


@app.route('/search/all', methods=["GET"])
def getAllUser():
    result = db.session.query(Person).all()

    return jsonify([nutzer.to_json() for nutzer in result])


@app.route('/search/p=<string:name>', methods=["GET"])
def searchUserByUsername(name):
    result = db.session.query(Person).filter_by(username=name)

    return jsonify([nutzer.to_json() for nutzer in result])


@app.route('/search/email=<string:email>', methods=["GET"])
def searchUserByEmail(email):
    result = db.session.query(Person).filter_by(email=email)

    return jsonify([nutzer.to_json() for nutzer in result])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
