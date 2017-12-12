from BLL.AirportsService import AirportsService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

airports_controller = Blueprint("airports_controller", __name__, url_prefix = "/api/Airports")
service = AirportsService()

@airports_controller.route("/GetAirports", methods=["GET"])
def get_airports():
    data = service.get_airports()
    return jsonify(data)

@airports_controller.route("/DeleteAirport", methods=["POST"])
def delete_airport():
    id = request.get_json();
    service.delete_airport(id)
    return 'Ok'

@airports_controller.route("/GetAirport", methods=["GET"])
def get_airport():
    id = request.args.get('id', '')
    data = service.get_airport(id)
    return jsonify(data)

@airports_controller.route("/AddAirport", methods=["POST"])
def add_airport():
    service.add_airport(request.get_json())
    return 'Ok'

@airports_controller.route("/IsCodeValid", methods=["Get"])
def is_code_valid():
    data = service.is_code_valid(request.args);
    if data[0].get('') == 'True':
        return jsonify(True)
    else:
       return jsonify(False)