from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class HotelsService(object):    
    def get_hotels_for_city(self, cityId):
        hotels = context.exec_param_sproc(context.GET_HOTELS_FOR_CITY_SPROC, [("cityId", cityId)])      
        for hotel in hotels:
            facilites = context.exec_param_sproc(context.GET_FACILITIES_FOR_HOTEL_SPROC,
                                                  [("hotelId", hotel.get("Id"))])
            facilities_list=[]
            for facility in facilites:
                facilities_list.append(facility.get("Name"))
            hotel["Facilities"] = facilities_list

            hotelPhotoes = context.exec_param_sproc(context.GET_PHOTOES_FOR_HOTEL_SPROC,
                                                  [("hotelId", hotel.get("Id"))])
            hotel["HotelPhotos"] = hotelPhotoes
        return hotels

    def get_hotel_short_info(self, id):
        hotels = context.exec_param_sproc(context.GET_HOTEL_SPROC, [("id", id)])    
        for hotel in hotels:
            facilites = context.exec_param_sproc(context.GET_FACILITIES_FOR_HOTEL_SPROC,
                                                  [("hotelId", hotel.get("Id"))])
            facilities_list=[]
            for facility in facilites:
                facilities_list.append(facility.get("Name"))
            hotel["Facilities"] = facilities_list

            hotelPhotoes = context.exec_param_sproc(context.GET_PHOTOES_FOR_HOTEL_SPROC,
                                                  [("hotelId", hotel.get("Id"))])
            hotel["HotelPhotos"] = hotelPhotoes
        return hotels[0]

    def get_room(self, roomId):
        room = context.exec_param_sproc(context.GET_ROOM_SPROC, [("roomId", roomId)])      
        return room[0]