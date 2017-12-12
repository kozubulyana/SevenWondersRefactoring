from BLL.SearchService import SearchService
from BLL.CitiesService import CitiesService
from BLL.HotelsService import HotelsService
from BLL.FlightsService import FlightsService
from BLL.AccountService import AccountService
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
from flask import session
import pdb
import datetime

search_controller = Blueprint("search_controller", __name__, url_prefix = "/api/Search")
searchService = SearchService()
citiesService = CitiesService()
hotelsService = HotelsService()
flightsService = FlightsService()
accountService = AccountService()

@search_controller.route("/GetTours", methods=["GET"])
def get_tours():
    countryFrom = request.args.get('countryFrom', '')
    countryTo = request.args.get('countryTo', '')
    people = int(request.args.get('people', ''))
    departureDate = request.args.get('departureDate', '')
    duration = int(request.args.get('duration', ''))
    cityFrom = request.args.get('cityFrom', '')
    cityTo = request.args.get('cityTo', '')

    arrivalDate_format = datetime.datetime.strptime(departureDate, "%Y-%m-%d") + datetime.timedelta(days=duration)
    arrivalDate = arrivalDate_format.strftime('%Y-%m-%d')

    departureCities = citiesService.get_cities(countryFrom, cityFrom)
    arrivalCities = citiesService.get_cities(countryTo, cityTo)

    tours=[]
    for cityDeparture in departureCities:
        for cityArrival in arrivalCities:
            hotels = hotelsService.get_hotels_for_city(cityArrival.get("Id"))
            freeSchedulesDeparture = searchService.get_free_schedules(cityDeparture.get("Id"),
                                                                   cityArrival.get("Id"),
                                                                   people,
                                                                   departureDate)
            freeSchedulesArrival = searchService.get_free_schedules(cityArrival.get("Id"),
                                                                   cityDeparture.get("Id"),
                                                                   people,
                                                                  arrivalDate)
            if len(hotels)!=0 and len(freeSchedulesDeparture)!=0 and len(freeSchedulesArrival)!=0:
                for hotel in hotels:
                    freeRooms = searchService.get_free_rooms_for_hotel(hotel.get("Id"),
                                                                       departureDate,
                                                                       arrivalDate,
                                                                       people)
                    if len(freeRooms)!=0:
                        flightShortInfoModel = {};

                        leaveFlightDepartureTime = departureDate + " " + freeSchedulesDeparture[0].get("DepartureTime").strftime('%H:%M')
                        returnFlightDepartureTime = arrivalDate + " " + freeSchedulesArrival[0].get("DepartureTime").strftime('%H:%M')

                        if freeSchedulesDeparture[0].get("ArrivalTime")<= freeSchedulesDeparture[0].get("DepartureTime") :
                            leaveFlightArrivalTime = (datetime.datetime.strptime(departureDate, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime('%Y-%m-%d') + " " + freeSchedulesDeparture[0].get("ArrivalTime").strftime('%H:%M')
                        else:
                            leaveFlightArrivalTime = departureDate + " " + freeSchedulesDeparture[0].get("ArrivalTime").strftime('%H:%M')

                        if freeSchedulesArrival[0].get("ArrivalTime")<= freeSchedulesArrival[0].get("DepartureTime") :
                            returnFlightArrivalTime = (arrivalDate_format + datetime.timedelta(days=1)).strftime('%Y-%m-%d') + " " + freeSchedulesArrival[0].get("ArrivalTime").strftime('%H:%M')
                        else:
                            returnFlightArrivalTime = arrivalDate + " " + freeSchedulesArrival[0].get("ArrivalTime").strftime('%H:%M')

                        flightShortInfoModel["LeaveFlightId"] = freeSchedulesDeparture[0].get("FlightId")
                        flightShortInfoModel["LeaveFlightPrice"] = freeSchedulesDeparture[0].get("FlightPrice")
                        flightShortInfoModel["LeaveFlightNumber"] = freeSchedulesDeparture[0].get("FlightNumber")
                        flightShortInfoModel["LeaveFlightAirplaneModel"] = freeSchedulesDeparture[0].get("FlightAirplaneModel")
                        flightShortInfoModel["LeaveFlightAirplaneCompany"] = freeSchedulesDeparture[0].get("FlightAirplaneCompany")
                        flightShortInfoModel["LeaveFlightDepartureAirport"] = freeSchedulesDeparture[0].get("FlightDepartureAirport")
                        flightShortInfoModel["LeaveFlightDepartureCity"] = cityDeparture.get("Name")
                        flightShortInfoModel["LeaveFlightDepartureCountry"] = cityDeparture.get("CountryName")
                        flightShortInfoModel["LeaveFlightDepartureTime"] = leaveFlightDepartureTime
                        flightShortInfoModel["LeaveFlightArrivalAirport"] = freeSchedulesDeparture[0].get("FlightArrivalAirport")
                        flightShortInfoModel["LeaveFlightArrivalCity"] = cityArrival.get("Name")
                        flightShortInfoModel["LeaveFlightArrivalCountry"] = cityArrival.get("CountryName")
                        flightShortInfoModel["LeaveFlightArrivalTime"] = leaveFlightArrivalTime

                        flightShortInfoModel["ReturnFlightId"] = freeSchedulesArrival[0].get("FlightId")
                        flightShortInfoModel["ReturnFlightPrice"] = freeSchedulesArrival[0].get("FlightPrice")
                        flightShortInfoModel["ReturnFlightNumber"] = freeSchedulesArrival[0].get("FlightNumber")
                        flightShortInfoModel["ReturnFlightAirplaneModel"] = freeSchedulesArrival[0].get("FlightAirplaneModel")
                        flightShortInfoModel["ReturnFlightAirplaneCompany"] = freeSchedulesArrival[0].get("FlightAirplaneCompany")
                        flightShortInfoModel["ReturnFlightDepartureAirport"] = freeSchedulesArrival[0].get("FlightDepartureAirport")
                        flightShortInfoModel["ReturnFlightDepartureCity"] = cityArrival.get("Name")
                        flightShortInfoModel["ReturnFlightDepartureCountry"] = cityArrival.get("CountryName")
                        flightShortInfoModel["ReturnFlightDepartureTime"] = returnFlightDepartureTime
                        flightShortInfoModel["ReturnFlightArrivalAirport"] = freeSchedulesArrival[0].get("FlightArrivalAirport")
                        flightShortInfoModel["ReturnFlightArrivalCity"] = cityDeparture.get("Name")
                        flightShortInfoModel["ReturnFlightArrivalCountry"] = cityDeparture.get("CountryName")
                        flightShortInfoModel["ReturnFlightArrivalTime"] = returnFlightArrivalTime

                        tour = {};
                        tour["People"] = people
                        tour["Duration"] = duration
                        tour["DepartureDate"] = datetime.datetime.strptime(departureDate, "%Y-%m-%d")
                        tour["ArrivaleDate"] = arrivalDate_format

                        tour["DepartureScheduleId"] = freeSchedulesDeparture[0].get("Id")
                        tour["ArrivalScheduleId"] = freeSchedulesArrival[0].get("Id")
                        tour["Hotel"] = hotel
                        tour["Flights"] = flightShortInfoModel
                        tour["Rooms"] = freeRooms
                        tours.append(tour); 
    result={};
    result["tours"]=tours
    if (session.get('role') == 1):
         result["isCustomer"] = True
    else:
         result["isCustomer"]= False
   
    return jsonify(result)

@search_controller.route("/BookTour", methods=["POST"])
def book_tour():
     personAmount = request.get_json().get("PersonAmount")
     leaveDate = request.get_json().get("LeaveDate")
     duration = request.get_json().get("Duration")
     roomId = request.get_json().get("RoomId")
     leaveScheduleId = request.get_json().get("LeaveScheduleId")
     returnScheduleId = request.get_json().get("ReturnScheduleId")
     withoutFood = request.get_json().get("WithoutFood")

     room = hotelsService.get_room(roomId)
     leaveSchedule = flightsService.get_schedule(leaveScheduleId)
     returnSchedule = flightsService.get_schedule(returnScheduleId)

     returnDate = (datetime.datetime.strptime(leaveDate, "%Y-%m-%d") + datetime.timedelta(days=duration)).strftime('%Y-%m-%d')
     if withoutFood:
         price = duration * (room.get("Price") + personAmount * room.get("FoodPrice")) + personAmount * (leaveSchedule.get("FlightPrice") + returnSchedule.get("FlightPrice"))
     else:
         price = duration * room.get("Price")  + personAmount * (leaveSchedule.get("FlightPrice") + returnSchedule.get("FlightPrice"))

     reservationId = searchService.add_reservation(roomId, personAmount, leaveScheduleId, returnScheduleId, leaveDate, returnDate, withoutFood)

     customerId = accountService.get_current_customer_id()
     creationDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
     searchService.add_tour(creationDate, price, reservationId, customerId)
     return 'Ok'