from BLL.AccountService import AccountService
from BLL.CustomerCabinetService import CustomerCabinetService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

customer_cabinet_controller = Blueprint("customer_cabinet_controller", __name__, url_prefix = "/api/CustomerCabinet")
accountService = AccountService()
customerCabinetService = CustomerCabinetService()

@customer_cabinet_controller.route("/GetCurrentCustomer", methods=["GET"])
def get_current_customer():
    customerId = accountService.get_current_customer_id()
    data = accountService.get_customer(customerId)
    return jsonify(data)

@customer_cabinet_controller.route("/EditCustomer", methods=["POST"])
def edit_customer():
    customer = request.form;
    customerId = accountService.get_current_customer_id()
    data = customerCabinetService.edit_customer(customerId, customer)
    return jsonify(data)        