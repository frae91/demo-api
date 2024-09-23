import os

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Customers(Resource):

    def get(self):
        customers = [customer.to_dict() for customer in Customer.query.all()]
        return make_response(jsonify(customers), 200)

    def post(self):
        new_customer = Customer(email_address=request.json.get('email_address'), name=request.json.get('name'), loyalty_number=request.json.get('loyalty_number'))

        db.session.add(new_customer)
        db.session.commit()

        if new_customer.id:
            return make_response(new_customer.to_dict(), 201)
        else:
            return make_response({"error": "Unable to create customer"}, 400)

class CustomerByEmail(Resource):
    def get(self, customer_email):
        
        customer = Customer.query.filter(Customer.email_address == customer_email).first()

        if customer:
            return make_response(customer.to_dict(), 200)

        return make_response({"error": "No customer found!"}, 404)


api.add_resource(Customers, '/customers')
api.add_resource(CustomerByEmail, '/customers/<string:customer_email>')