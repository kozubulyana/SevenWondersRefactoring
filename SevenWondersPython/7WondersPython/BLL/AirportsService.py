from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class AirportsService(object):
    def get_airports(self):        
        airports = context.exec_no_param_sproc(context.GET_AIRPORTS_SPROC)
        return airports
  
    def delete_airport(self, id):
        context.exec_param_sproc(context.DELETE_AIRPORT_SPROC, [("id", id)])
        return

    def get_airport(self, id):
        city = context.exec_param_sproc(context.GET_AIRPORT_SPROC, [("id", id)])
        return city[0]

    def add_airport(self, city):       
        id= city.get("Id");
        name = str(city.get("Name"));
        code = city.get("Code");
        cityId = city.get("CityId");
        context.exec_param_sproc(context.ADD_AIRPORT_SPROC, [("id", id), ("name", name), ("code", code), ("cityId", cityId)])
        return

    def is_code_valid(self, city):
        id = city.get("id");
        code = city.get("code");
        isValid = context.exec_param_sproc(context.IS_AIRPORT_CODE_VALID_SPROC, [("id", id), ("code", code)])
        return isValid;


