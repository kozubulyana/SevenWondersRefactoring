from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class CountryItem:
    Id = 0
    Text = ""
    IsChecked = ""
    def convert_to_dictionary_item(self):
        result = dict()
        result["Id"] = self.Id
        result["Text"] = self.Text
        result["IsChecked"] = self.IsChecked
        return result

def convert_country_to_items(id, name):
    item = CountryItem()
    item.Id = id
    item.Text = name
    item.IsChecked = False
    return item

class ManagersService(object):
    def get_managers(self):        
        managers = context.exec_no_param_sproc(context.GET_MANAGERS_SPROC)
        return managers

    def get_countries(self):
        countries = context.exec_no_param_sproc(context.GET_COUNTRIES_SPROC)
        return countries

    def get_manager(self, id):
        manager = context.exec_param_sproc(context.GET_MANAGER_SPROC, [("id", id)])
        all_countries = self.get_countries()
        manager_countries = self.get_countries_for_manager(id)
        result_countries = []
        manager_ids = []
        for country in all_countries:
            result_countries.append(convert_country_to_items(country["Id"], country["Name"]))
        for country in manager_countries:
            manager_ids.append(country["Id"])
        for res in result_countries:
            if (manager_ids.count(res.Id) > 0):
                res.IsChecked = True
        final_result = []
        for res in result_countries:
            final_result.append(res.convert_to_dictionary_item())
        manager[0]["Countries"] = final_result
        return manager

    def get_countries_for_manager(self,id):
        countries = context.exec_param_sproc(context.GET_COUNTRIES_FOR_MANAGER_SPROC, [("id", id)])
        return countries

    def change_manager_status(self, id):
        context.exec_param_sproc(context.CHANGE_MANAGER_STATUS_SPROC, [("id", id)])
        return

    def add_manager(self, immutableDictForm):
        countries = immutableDictForm.getlist("countries[]")
        id = immutableDictForm.get("manager[Id]")
        firstName = immutableDictForm.get("manager[FirstName]")
        lastName = immutableDictForm.get("manager[LastName]")
        dateOfBirth = immutableDictForm.get("manager[DateOfBirth]")
        phoneNumber = immutableDictForm.get("manager[PhoneNumber]")
        email = immutableDictForm.get("manager[Email]")
        password = immutableDictForm.get("manager[Password]")
        countriesList = ",".join(countries)
        context.exec_param_sproc(context.ADD_MANAGER_SPROC,
                                 [("id", id),
                                  ("firstName", firstName),
                                  ("lastName", lastName),
                                  ("dateOfBirth", str(dateOfBirth)),
                                  ("phoneNumber", phoneNumber),
                                  ("email", str(email)),
                                  ("password", str(password)),
                                  ("countriesList", str(countriesList))])
        return

