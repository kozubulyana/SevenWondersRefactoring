from BLL.ToursService import ToursService
from BLL.AccountService import AccountService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

tours_management_controller = Blueprint("tours_management_controller", __name__, url_prefix = "/api/ToursManagement")
toursService = ToursService()
accountService = AccountService()

@tours_management_controller.route("/GetToursForManager", methods=["GET"])
def get_tours_for_manager():
    pageIndex = int(request.args.get('pageIndex', 0))
    pageSize = int(request.args.get('pageSize', 10))
    managerId = accountService.get_current_manager_id()
    tours =  toursService.get_tours_for_manager(managerId)
    dataCount = len(tours)

    tours=tours[pageSize*pageIndex:(pageIndex+1)*pageSize]
    result = {};
    result["tours"] = tours
    result["dataCount"] = dataCount
    return jsonify(result)

@tours_management_controller.route("/GetToursForCustomer", methods=["GET"])
def get_tours_for_customer():
    pageIndex = int(request.args.get('pageIndex', 0))
    pageSize = int(request.args.get('pageSize', 10))

    customerId = accountService.get_current_customer_id()
    tours =  toursService.get_tours_for_customer(customerId)
    dataCount = len(tours)

    tours=tours[pageSize*pageIndex:(pageIndex+1)*pageSize]
    result = {};
    result["tours"] = tours
    result["dataCount"] = dataCount
    return jsonify(result)

@tours_management_controller.route("/DeleteTour", methods=["POST"])
def delete_tour():
    tourId = request.get_json()
    toursService.delete_tour(tourId)
    return 'Ok'

@tours_management_controller.route("/PayForTour", methods=["POST"])
def pay_for_tour():
    tourId = request.get_json()
    toursService.pay_for_tour(tourId)
    return 'Ok'
