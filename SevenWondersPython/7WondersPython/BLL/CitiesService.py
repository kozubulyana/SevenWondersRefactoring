from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class CitiesService(object):
    def get_cities(self, countryId, cityId):
        if countryId=='':
           cities = context.exec_no_param_sproc(context.GET_CITIES_SPROC)
        elif cityId=='':
           cities = context.exec_param_sproc(context.GET_CITIES_SPROC, [("countryId", countryId) ])
        else:
           cities = context.exec_param_sproc(context.GET_CITIES_SPROC, [("countryId", countryId),("cityId", cityId) ])
        
        return cities
  
    def delete_city(self, id):
        context.exec_param_sproc(context.DELETE_CITY_SPROC, [("id", id)])
        return

    def get_city(self, id):
        city = context.exec_param_sproc(context.GET_CITY_SPROC, [("id", id)])
        return city[0]

    def add_city(self, city):   
        id= city.get("Id");
        name = str(city.get("Name"));
        countryId = city.get("CountryId");
        context.exec_param_sproc(context.ADD_CITY_SPROC, [("id", id), ("name", name), ("countryId", countryId)])
        return

    def is_name_valid(self, city):
        id = city.get("id");
        name = str(city.get("name"));
        countryId = city.get("countryId");
        isValid = context.exec_param_sproc(context. IS_CITY_NAME_VALID_SPROC, [("id", id), ("name", name), ("countryId", countryId)])
        return isValid;


