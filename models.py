from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    loyalty_number = db.Column(db.String)

    def __repr__(self):
        return f"<Customer {self.id}: {self.email_address}"
