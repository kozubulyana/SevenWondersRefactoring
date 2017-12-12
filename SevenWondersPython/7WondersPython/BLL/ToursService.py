from DAL.SevenWondersContext import SevenWondersContext
import itertools

context = SevenWondersContext()
class ToursService(object):    
    def get_tours_for_manager(self, managerId):
        tours = context.exec_param_sproc(context.GET_TOURS_FOR_MANAGER_SPROC, [("managerId", managerId)])  
        return tours

    def get_tours_for_customer(self,customerId):
        tours = context.exec_param_sproc(context.GET_TOURS_FOR_CUSTOMER_SPROC, [("customerId", customerId)])  
        return tours

    def get_tour(self, id):
        tour = context.exec_param_sproc(context.GET_TOUR_SPROC, [("id", id)])  
        return tour[0]

    def delete_tour(self, id):
        context.exec_param_sproc(context.DELETE_TOUR_SPROC, [("id", id)])  
        return

    def pay_for_tour(self, id):
        context.exec_param_sproc(context.PAY_FOR_TOUR_SPROC, [("id", id)])  
        return