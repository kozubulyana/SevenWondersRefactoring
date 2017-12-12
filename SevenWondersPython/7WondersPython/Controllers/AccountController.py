from BLL.AccountService import AccountService
from flask import session
from flask import Blueprint, jsonify, request, abort 

account_controller = Blueprint("account_controller", __name__, url_prefix = "/api/Account")
service = AccountService()

@account_controller.route("/Login", methods=["POST"])
def login():
    succeeded = service.login(request.form)
    if (succeeded == True):
        return 'Ok'
    else:
        return abort(400)

@account_controller.route("/LogOut", methods=["POST"])
def logout():
    service.logout()
    return 'Ok'

@account_controller.route("/GetUserRole", methods=["GET"])
def get_user_role():
    role = session.get('role')
    if role == 1:
        return "customer"
    elif role == 2:
        return "admin"
    elif role == 3:
        return "manager"
    else:
        return ""

@account_controller.route("/Register", methods=["POST"])
def register():
    service.register(request.form)
    return 'Ok'