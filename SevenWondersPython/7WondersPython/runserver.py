import os
from os import environ
from flask import Flask, json, Response
from flask import render_template, session
from Controllers.ManagersController import managers_controller
from Controllers.CustomersController import customers_controller
from Controllers.CountriesController import countries_controller
from Controllers.CitiesController import cities_controller
from Controllers.AirportsController import airports_controller
from Controllers.SearchController import search_controller
from Controllers.ToursManagementController import tours_management_controller
from Controllers.HotelsController import hotels_controller
from Controllers.FlightsController import flights_controller
from Controllers.CustomerCabinetController import customer_cabinet_controller
from Controllers.AccountController import account_controller

from flask_jwt_extended import JWTManager
from Helpers.json_helper import json_types_handler
from jinja2 import TemplateNotFound

app = Flask(__name__, template_folder='templates')
app.config['JWT_SECRET_KEY'] = "YLU]o:qifk]Z17{H'l2hIC?7_YbQ]"
jwt = JWTManager(app)

wsgi_app = app.wsgi_app
app.register_blueprint(managers_controller)
app.register_blueprint(customers_controller)
app.register_blueprint(countries_controller)
app.register_blueprint(cities_controller)
app.register_blueprint(airports_controller)
app.register_blueprint(search_controller)
app.register_blueprint(tours_management_controller)
app.register_blueprint(hotels_controller)
app.register_blueprint(flights_controller)
app.register_blueprint(customer_cabinet_controller)
app.register_blueprint(account_controller)

json.JSONEncoder.default = json_types_handler

@app.route('/')
def index():
    data = {
        "title": 'Home Page',
        "msg":'GG wp',
        "me": environ.get('USERNAME')}
    return render_template('Views/Home/Index.html',data=data)

@app.route('/Views/ManagersManagement/Index.html')
def html_managers_management_lookup():
    try:
        return render_template('Views/ManagersManagement/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/CustomersManagement/Index.html')
def html_customers_management_lookup():
    try:
        return render_template('Views/CustomersManagement/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Countries/Index.html')
def html_countries_lookup():
    try:
        return render_template('Views/Countries/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Cities/Index.html')
def html_cities_lookup():
    try:
        return render_template('Views/Cities/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Airports/Index.html')
def html_airports_lookup():
    try:
        return render_template('Views/Airports/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Search/Index.html')
def html_search_lookup():
    try:
        return render_template('Views/Search/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Search/Booking.html')
def html_booking_lookup():
    try:
        return render_template('Views/Search/Booking.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Home/Contact.html')
def html_contact_lookup():
    try:
        return render_template('Views/Home/Contact.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Hotels/HotelShortInfo.html')
def html_hotel_short_info_lookup():
    try:
        return render_template('Views/Hotels/HotelShortInfo.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Hotels/RoomShortInfo.html')
def html_room_short_info_lookup():
    try:
        return render_template('Views/Hotels/RoomShortInfo.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Flights/FlightShortInfo.html')
def html_flight_short_info_lookup():
    try:
        return render_template('Views/Flights/FlightShortInfo.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/ToursManagement/Index.html')
def html_toours_management_lookup():
    try:
        return render_template('Views/ToursManagement/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Flights/Index.html')
def html_flights_lookup():
    try:
        return render_template('Views/Flights/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/CustomerCabinet/Index.html')
def html_customer_cabinet_lookup():
    try:
        return render_template('Views/CustomerCabinet/Index.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Account/Login.html')
def html_login_lookup():
    try:
        return render_template('Views/Account/Login.html')
    except TemplateNotFound:
        abort(404)

@app.route('/Views/Account/Register.html')
def html_register_lookup():
    try:
        return render_template('Views/Account/Register.html')
    except TemplateNotFound:
        abort(404)
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.secret_key = os.urandom(12)
    app.run(HOST, PORT, debug=False, threaded=True)