from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class SearchService(object):    
    def get_free_rooms_for_hotel(self, hotelId, departureDate, arrivalDate, people):
        rooms = context.exec_param_sproc(context.GET_FREE_ROOMS_FOR_HOTEL_SPROC, 
                                         [("hotelId", hotelId),
                                          ("departureDate", departureDate),
                                          ("arrivalDate", arrivalDate),
                                          ("people", people)])  
        for room in rooms:
            room["Price"]=float(room.get("Price"))
            equipments = context.exec_param_sproc(context.GET_EQUIPMENTS_FOR_ROOM_SPROC,
                                                  [("roomId", room.get("Id"))])
            equipments_list=[]
            for equipment in equipments:
                equipments_list.append(equipment.get("Name"))
            room["Equipments"] = equipments_list

            roomPhotoes = context.exec_param_sproc(context.GET_PHOTOES_FOR_ROOM_SPROC,
                                                  [("roomId", room.get("Id"))])
            room["RoomPhotos"] = roomPhotoes
        return rooms

    def get_free_schedules(self, cityDepartureId, cityArrivalId, people, date):
        schedules = context.exec_param_sproc(context.GET_FREE_SCHEDULES_SPROC, 
                                         [("cityDepartureId", cityDepartureId),
                                          ("cityArrivalId", cityArrivalId),
                                          ("people", people),
                                          ("date", date)])     
                  
        for schedule in schedules:
            schedule["FlightPrice"]=float(schedule.get("FlightPrice"))
        return schedules

    def add_reservation(self, roomId, personAmount, leaveScheduleId, returnScheduleId, leaveDate, returnDate, withoutFood):
        return context.exec_param_sproc(context.ADD_RESERVATION_SPROC, 
                                         [("roomId", roomId),
                                          ("personAmount", personAmount),
                                          ("leaveScheduleId", leaveScheduleId),
                                          ("returnScheduleId", returnScheduleId),
                                          ("leaveDate", leaveDate),
                                          ("returnDate", returnDate),
                                          ("withoutFood", withoutFood)])[0].get("Id")

    def add_tour(self, creationDate, totalPrice, reservationId, customerId):
        context.exec_param_sproc(context.ADD_TOUR_SPROC, 
                                         [("creationDate", creationDate),
                                          ("totalPrice", totalPrice),
                                          ("reservationId", reservationId),
                                          ("customerId", customerId)])
        return