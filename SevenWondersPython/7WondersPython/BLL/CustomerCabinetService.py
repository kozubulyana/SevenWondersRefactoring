from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class CustomerCabinetService(object):
    def edit_customer(self, id, customer):
        firstName = customer.get("FirstName")
        lastName = customer.get("LastName")
        dateOfBirth = customer.get("DateOfBirth")
        phoneNumber = customer.get("PhoneNumber")
        email = customer.get("Email")

        context.exec_param_sproc(context.EDIT_CUSTOMER_SPROC, 
                                 [("id", id),
                                  ("firstName", firstName),
                                  ("lastName", lastName),
                                  ("dateOfBirth", dateOfBirth),
                                  ("phoneNumber", phoneNumber),
                                  ("email", email)])
        return
