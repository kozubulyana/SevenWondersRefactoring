from BLL.HotelsService import HotelsService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb

hotels_controller = Blueprint("hotels_controller", __name__, url_prefix = "/api/Hotels")
service = HotelsService()

@hotels_controller.route("/GetHotelShortInfo", methods=["GET"])
def get_hotel_short_info():
    id = request.args.get('id', 0)
    data = service.get_hotel_short_info(id)
    return jsonify(data)
