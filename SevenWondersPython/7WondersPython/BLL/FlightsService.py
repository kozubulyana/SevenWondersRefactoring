from DAL.SevenWondersContext import SevenWondersContext

import itertools

context = SevenWondersContext()
class FlightsService(object):    
    def get_schedule(self, scheduleId):       
        schedule = context.exec_param_sproc(context.GET_SCHEDULE_SPROC, [("id", scheduleId)])      
        return schedule[0]
    
    def get_flights(self):       
        flights = context.exec_no_param_sproc(context.GET_FLIGHTS_SPROC)      
        return flights

    def get_schedules(self, flightId):       
        schedules = context.exec_param_sproc(context.GET_SCHEDULES_SPROC, [("flightId", flightId)])      
        return schedules

    def delete_flight(self, flightId):       
        context.exec_param_sproc(context.DELETE_FLIGHT_SPROC, [("id", flightId)])      
        return

    def is_number_valid(self, flight):
        id = flight.get("id");
        number = flight.get("number");
        isValid = context.exec_param_sproc(context.IS_FLIGHT_NUMBER_VALID_SPROC, [("id", id), ("number", number)])
        return isValid;

    def add_flight(self, flight):
        number = flight.get("number");
        price = flight.get("price");
        departureAirportId = flight.get("departureAirportId");
        arrivalAirportId = flight.get("arrivalAirportId");
        model = str(flight.get("airplaneModel"));
        company = str(flight.get("airplaneCompany"));
        seatsAmount = flight.get("seatsAmount");

        airplaneId = context.exec_param_sproc(context.ADD_AIRPLANE_SPROC,
                                [("model", model),
                                ("company", company),
                                ("seatsAmount", seatsAmount)])[0].get("Id")

        context.exec_param_sproc(context.ADD_FLIGHT_SPROC,
                                [("number", number),
                                ("price", price),
                                ("airplaneId", airplaneId),
                                ("departureAirportId", departureAirportId),
                                ("arrivalAirportId", arrivalAirportId)])
        return

    def edit_flight(self, flight):
        id = flight.get("id");
        number = flight.get("number");
        price = flight.get("price");
        departureAirportId = flight.get("departureAirportId");
        arrivalAirportId = flight.get("arrivalAirportId");
        airplaneId = flight.get("airplaneId");
        model = str(flight.get("airplaneModel"));
        company = str(flight.get("airplaneCompany"));
        seatsAmount = flight.get("seatsAmount");

        context.exec_param_sproc(context.EDIT_AIRPLANE_SPROC,
                                [("id", airplaneId),
                                ("model", model),
                                ("company", company),
                                ("seatsAmount", seatsAmount)])

        context.exec_param_sproc(context.EDIT_FLIGHT_SPROC,
                                [("id", id),
                                ("number", number),
                                ("price", price),
                                ("departureAirportId", departureAirportId),
                                ("arrivalAirportId", arrivalAirportId)])
        return

    def delete_schedule(self, scheduleId):       
        context.exec_param_sproc(context.DELETE_SCHEDULE_SPROC, [("id", scheduleId)])      
        return

    def edit_schedule(self, schedule):     
        id = schedule.get("Id");
        dayOfWeek = schedule.get("DayOfWeek");
        departureTime = schedule.get("DepartureTime");
        arrivalTime = schedule.get("ArrivalTime");

        context.exec_param_sproc(context.EDIT_SCHEDULE_SPROC, 
                                 [("id", id),
                                  ("dayOfWeek", dayOfWeek),
                                  ("departureTime", departureTime),
                                  ("arrivalTime", arrivalTime),])      
        return

    def add_schedule(self, flightId, schedule):     
        flightId = flightId;
        dayOfWeek = schedule.get("DayOfWeek");
        departureTime = schedule.get("DepartureTime");
        arrivalTime = schedule.get("ArrivalTime");

        context.exec_param_sproc(context.ADD_SCHEDULE_SPROC, 
                                 [("flightId", flightId),
                                  ("dayOfWeek", dayOfWeek),
                                  ("departureTime", departureTime),
                                  ("arrivalTime", arrivalTime),])      
        return