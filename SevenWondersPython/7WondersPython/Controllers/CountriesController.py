from BLL.CountriesService import CountriesService
from Helpers.RPCClient import rpcClientOut
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

countries_controller = Blueprint("countries_controller", __name__, url_prefix = "/api/Countries")
service = CountriesService()

@countries_controller.route("/GetCountries", methods=["GET"])
def get_countries():
    result = rpcClientOut.get_data("7")
    return result

@countries_controller.route("/GetCountry", methods=["GET"])
def get_country():
    data = service.get_country(request.args.get('id', ''))[0]
    return jsonify(data)

@countries_controller.route("/AddCountry", methods=["POST"])
def add_country():
    service.add_country(request.get_json())
    return 'Ok'

@countries_controller.route("/IsNameValid", methods=["Get"])
def is_name_valid():
    data = service.is_name_valid(request.args);
    if data[0].get('') == 'True':
        return jsonify(True)
    else:
       return jsonify(False)

@countries_controller.route("/DeleteCountry", methods=["POST"])
def delete_country():
    id = request.get_json();
    service.delete_country(id)
    return 'Ok'