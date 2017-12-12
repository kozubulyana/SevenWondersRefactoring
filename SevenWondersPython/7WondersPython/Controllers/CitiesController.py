from BLL.CitiesService import CitiesService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

cities_controller = Blueprint("cities_controller", __name__, url_prefix = "/api/Cities")
service = CitiesService()

@cities_controller.route("/GetCities", methods=["GET"])
def get_cities():
    countryId = request.args.get('countryId', '')
    cityId = request.args.get('cityId', '')
    data = service.get_cities(countryId, cityId)
    return jsonify(data)

@cities_controller.route("/DeleteCity", methods=["POST"])
def delete_city():
    id = request.get_json();
    service.delete_city(id)
    return 'Ok'

@cities_controller.route("/GetCity", methods=["GET"])
def get_city():
    id = request.args.get('id', '')
    data = service.get_city(id)
    return jsonify(data)

@cities_controller.route("/AddCity", methods=["POST"])
def add_city():
    service.add_city(request.get_json())
    return 'Ok'

@cities_controller.route("/IsNameValid", methods=["Get"])
def is_name_valid():
    data = service.is_name_valid(request.args);
    if data[0].get('') == 'True':
        return jsonify(True)
    else:
       return jsonify(False)