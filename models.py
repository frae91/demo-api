from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    serialize_rules = ('-reservations.customer',)

    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    loyalty_number = db.Column(db.String)

    reservations = db.relationship('Reservation', back_populates='customer')

    def __repr__(self):
        return f"<Customer {self.id}: {self.email_address}"

class Reservation(db.Model, SerializerMixin):
    __tablename__ = "reservations"

    serialize_rules = ('-customer.reservations',)

    id = db.Column(db.Integer, primary_key=True)
    check_in_date = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    customer = db.relationship('Customer', back_populates='reservations')

    def __repr__(self):
        return f"<Reservation by {customer.name} on {self.check_in_date} for {self.duration} nights>"
