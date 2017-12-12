from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class CustomersService(object):
    def get_customers(self):        
        customers = context.exec_no_param_sproc(context.GET_CUSTOMERS_SPROC)
        return customers

    def change_customer_status(self, id):
        context.exec_param_sproc(context.CHANGE_CUSTOMER_STATUS_SPROC, [("id", id)])
        return