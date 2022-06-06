from flask_sqlalchemy import SQLAlchemy
import uuid

from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()


class Order(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String, unique=True, nullable=False)
    #person_id = db.Column(UUID(as_uuid=True), db.ForeignKey('nutzer.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Order: {self.id}>'

    def to_json(self):
        return {
            'id ': self.id,
            'name ': self.name
        }
    