from BLL.FlightsService import FlightsService
from BLL.AirportsService import AirportsService
from BLL.ToursService import ToursService
from BLL.ToursService import ToursService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
import pdb
import datetime

flights_controller = Blueprint("flights_controller", __name__, url_prefix = "/api/Flights")
flightsService = FlightsService()
airportsService = AirportsService()
toursService = ToursService()

@flights_controller.route("/GetFlightsShortInfo", methods=["GET"])
def get_flights_short_info():
    tourId = request.args.get('id', 0)
    tour = toursService.get_tour(tourId)

    leaveSchedule = flightsService.get_schedule(tour.get("LeaveScheduleId"))
    returnSchedule = flightsService.get_schedule(tour.get("ReturnScheduleId"))

    leaveFlightDepartureTime = tour.get("LeaveDate").strftime('%Y-%m-%d') + " " + leaveSchedule.get("DepartureTime").strftime('%H:%M')
    returnFlightDepartureTime = tour.get("ReturnDate").strftime('%Y-%m-%d') + " " + returnSchedule.get("DepartureTime").strftime('%H:%M')

    if leaveSchedule.get("ArrivalTime")<= leaveSchedule.get("DepartureTime") :
        leaveFlightArrivalTime = (tour.get("LeaveDate")+ datetime.timedelta(days=1)).strftime('%Y-%m-%d') + " " + leaveSchedule.get("ArrivalTime").strftime('%H:%M')
    else:
        leaveFlightArrivalTime = tour.get("LeaveDate").strftime('%Y-%m-%d') + " " + leaveSchedule.get("ArrivalTime").strftime('%H:%M')

    if returnSchedule.get("ArrivalTime")<= returnSchedule.get("DepartureTime") :
        returnFlightArrivalTime = (tour.get("ReturnDate") + datetime.timedelta(days=1)).strftime('%Y-%m-%d') + " " + returnSchedule.get("ArrivalTime").strftime('%H:%M')
    else:
        returnFlightArrivalTime = tour.get("ReturnDate").strftime('%Y-%m-%d') + " " + returnSchedule.get("ArrivalTime").strftime('%H:%M')

    flightShortInfoModel = {}
    flightShortInfoModel["LeaveFlightId"] = leaveSchedule.get("FlightId")
    flightShortInfoModel["LeaveFlightPrice"] = leaveSchedule.get("FlightPrice")
    flightShortInfoModel["LeaveFlightNumber"] = leaveSchedule.get("FlightNumber")
    flightShortInfoModel["LeaveFlightAirplaneModel"] = leaveSchedule.get("FlightAirplaneModel")
    flightShortInfoModel["LeaveFlightAirplaneCompany"] = leaveSchedule.get("FlightAirplaneCompany")
    flightShortInfoModel["LeaveFlightDepartureAirport"] = leaveSchedule.get("FlightDepartureAirport")
    flightShortInfoModel["LeaveFlightDepartureCity"] = tour.get("DepartureCity")
    flightShortInfoModel["LeaveFlightDepartureCountry"] = tour.get("DepartureCountry")
    flightShortInfoModel["LeaveFlightDepartureTime"] = leaveFlightDepartureTime
    flightShortInfoModel["LeaveFlightArrivalAirport"] = leaveSchedule.get("FlightArrivalAirport")
    flightShortInfoModel["LeaveFlightArrivalCity"] = tour.get("ArrivalCity")
    flightShortInfoModel["LeaveFlightArrivalCountry"] = tour.get("ArrivalCountry")
    flightShortInfoModel["LeaveFlightArrivalTime"] = leaveFlightArrivalTime

    flightShortInfoModel["ReturnFlightId"] = returnSchedule.get("FlightId")
    flightShortInfoModel["ReturnFlightPrice"] = returnSchedule.get("FlightPrice")
    flightShortInfoModel["ReturnFlightNumber"] = returnSchedule.get("FlightNumber")
    flightShortInfoModel["ReturnFlightAirplaneModel"] = returnSchedule.get("FlightAirplaneModel")
    flightShortInfoModel["ReturnFlightAirplaneCompany"] = returnSchedule.get("FlightAirplaneCompany")
    flightShortInfoModel["ReturnFlightDepartureAirport"] = returnSchedule.get("FlightDepartureAirport")
    flightShortInfoModel["ReturnFlightDepartureCity"] = tour.get("ArrivalCity")
    flightShortInfoModel["ReturnFlightDepartureCountry"] = tour.get("ArrivalCountry")
    flightShortInfoModel["ReturnFlightDepartureTime"] = returnFlightDepartureTime
    flightShortInfoModel["ReturnFlightArrivalAirport"] = returnSchedule.get("FlightArrivalAirport")
    flightShortInfoModel["ReturnFlightArrivalCity"] = tour.get("DepartureCity")
    flightShortInfoModel["ReturnFlightArrivalCountry"] = tour.get("DepartureCountry")
    flightShortInfoModel["ReturnFlightArrivalTime"] = returnFlightArrivalTime
    return jsonify(flightShortInfoModel)

@flights_controller.route("/GetFlights", methods=["GET"])
def get_flights():
    pageIndex = int(request.args.get('pageIndex', 0))
    pageSize = int(request.args.get('pageSize', 10))
    flights = flightsService.get_flights()
    dataCount = len(flights)

    flights=flights[pageSize*pageIndex:(pageIndex+1)*pageSize]
    result = {};
    result["flights"] = flights
    result["dataCount"] = dataCount
    return jsonify(result)

@flights_controller.route("/GetAirports", methods=["GET"])
def get_airoports():
    airoports = airportsService.get_airports()
    for airoport in airoports:
        airoport["Text"] = airoport.get("Name")
    return jsonify(airoports)

@flights_controller.route("/GetSchedules", methods=["GET"])
def get_schedules():
    flightId = int(request.args.get('id', 0))
    schedules = flightsService.get_schedules(flightId)
    return jsonify(schedules)

@flights_controller.route("/DeleteFlight", methods=["POST"])
def delete_flight():
    flightId = int(request.get_json())
    flightsService.delete_flight(flightId)
    return "Ok"

@flights_controller.route("/IsNumberValid", methods=["Get"])
def is_number_valid():
    data = flightsService.is_number_valid(request.args);
    if data[0].get('') == 'True':
        return jsonify(True)
    else:
       return jsonify(False)

@flights_controller.route("/AddFlight", methods=["POST"])
def add_flight():
    flightsService.add_flight(request.get_json())
    return 'Ok'

@flights_controller.route("/EditFlight", methods=["POST"])
def edit_flight():
    flightsService.edit_flight(request.get_json())
    return 'Ok'

@flights_controller.route("/EditSchedule", methods=["POST"])
def edit_schedule():
    flightId = request.get_json().get("flightId")
    schedules = request.get_json().get("schedule");

    oldSchedules = flightsService.get_schedules(flightId)
    for schedule in oldSchedules:
        flightsService.delete_schedule(schedule.get("Id"))
    
    for schedule in schedules:
        if schedule.get("Id") == -1:
            flightsService.add_schedule(flightId, schedule)
        else: 
            flightsService.edit_schedule(schedule)
    return 'Ok'