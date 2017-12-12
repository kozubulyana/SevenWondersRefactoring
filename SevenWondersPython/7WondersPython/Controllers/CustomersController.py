from BLL.CustomersService import CustomersService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

customers_controller = Blueprint("customers_controller", __name__, url_prefix = "/api/Customers")
service = CustomersService()

@customers_controller.route("/GetCustomers", methods=["GET"])
def get_customers():
    data = service.get_customers()
    return jsonify(data)

@customers_controller.route("/ChangeCustomerStatus/<int:id>", methods=["POST"])
def change_customer_status(id):
    service.change_customer_status(id)
    return 'Ok'