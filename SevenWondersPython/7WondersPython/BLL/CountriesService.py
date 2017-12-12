from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class CountriesService(object):
    def get_countries(self):
        countries = context.exec_no_param_sproc(context.GET_COUNTRIES_SPROC)
        return countries

    def get_country(self, id):
        country = context.exec_param_sproc(context.GET_COUNTRY_SPROC, [("id", id)])
        return country

    def add_country(self, country): 
        id= country.get("id");
        name = str(country.get("name"));
        context.exec_param_sproc(context.ADD_COUNTRY_SPROC, [("id", id), ("name", name)])
        return

    def is_name_valid(self, country):
        id = country.get("id");
        name = str(country.get("name"));
        isValid = context.exec_param_sproc(context.IS_COUNTRY_NAME_VALID_SPROC, [("id", id), ("name", name)])
        return isValid;

    def delete_country(self, id):
        context.exec_param_sproc(context.DELETE_COUNTRY_SPROC, [("id", id)])
        return