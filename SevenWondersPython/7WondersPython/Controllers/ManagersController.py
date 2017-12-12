from BLL.ManagersService import ManagersService
from flask import Blueprint, jsonify, request, session
from flask_jwt_extended import get_jwt_identity
from Helpers.RPCClient import rpcClientOut
import pika
import uuid
import threading
from time import sleep
import pdb

managers_controller = Blueprint("managers_controller", __name__, url_prefix = "/api/Managers")
service = ManagersService()

@managers_controller.route("/GetManagers", methods=["POST"])
def get_managers():
    #data = service.get_managers()
    corrid = rpcClientOut.send_request("info")
    while rpcClientOut.queue[corrid] is None:
        sleep(0.1)
    data = rpcClientOut.queue[corrid].decode('utf-8')
    return jsonify(data)

@managers_controller.route("/GetCountries", methods=["GET"])
def get_countries():
    data = service.get_countries()
    return jsonify(data)

@managers_controller.route("/GetManager/<int:id>", methods=["GET"])
def get_manager(id):
    data = service.get_manager(id)
    result = data[0]
    return jsonify(result)

@managers_controller.route("/ChangeManagerStatus/<int:id>", methods=["POST"])
def change_manager_status(id):
    service.change_manager_status(id)
    return 'Ok'

@managers_controller.route("/AddManager", methods=["POST"])
def add_manager():
    service.add_manager(request.form)
    return 'Ok'

