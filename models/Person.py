from flask_sqlalchemy import SQLAlchemy
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Nutzer(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    orders = db.relationship("order", backref="nutzer", lazy=True)

    def __repr__(self):
        return f'<Nutzer: {self.id}>'

    def to_json(self):
        return {
            'id ': self.id,
            'username ': self.username,
            'email ': self.email,
            'order ':  self.order
        }
