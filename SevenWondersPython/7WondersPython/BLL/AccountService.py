from DAL.SevenWondersContext import SevenWondersContext
from flask import session
import itertools
import hashlib
import base64

context = SevenWondersContext()
class AccountService(object):
    def get_customer(self, id):        
        customer = context.exec_param_sproc(context.GET_CUSTOMER_SPROC, [("id", id) ])
        return customer[0]
  
    def login(self, dictform):
        email = dictform.get("Email")
        password = dictform.get("Password")

        p = self.hash_password(password).decode()
        current_user = context.exec_param_sproc(context.GET_USER_SPROC, [("email", str(email)),
                                                                   ("hashedPassword", p)])      
        if (current_user == []):
            return False;
        role = current_user[0]["RoleId"]
        id = current_user[0]["Id"]

        #customer
        if (role == 1):
            customer = context.exec_param_sproc(context.GET_CUSTOMER_BY_EMAIL_SPROC, [("email", str(email))])
            if (customer[0]["IsDeleted"] == 0):
                session["id"] = id
                session["role"] = role
                return True
            else:
                return False
        #admin
        elif (role == 2):
            session["id"] = id
            session["role"] = role
            return True
        #manager
        elif (role == 3):
            manager = context.exec_param_sproc(context.GET_MANAGER_BY_EMAIL_SPROC, [("email", str(email))])
            if (manager[0]["IsDeleted"] == 0):
                session["id"] = id
                session["role"] = role
                return True
            else:
                return False

    def logout(self):
        session.clear()

    def hash_password(self, pwd):
        pswd = pwd + "blabla"
        password = hashlib.md5()
        password.update(pswd.encode('utf-8'))
        res = password.digest()[:16]
        endres64 = base64.b64encode(res)
        return endres64[:len(endres64) - 2]

    def get_current_manager_id(self):
        id = session.get('id')
        user = context.exec_param_sproc(context.GET_USER_BY_ID_SPROC, [("id", id)]) [0] 
        manager = context.exec_param_sproc(context.GET_MANAGER_BY_EMAIL_SPROC, [("email", user.get("Email"))])[0]
        return manager.get("Id")

    def get_current_customer_id(self):
        id = session.get('id')
        user = context.exec_param_sproc(context.GET_USER_BY_ID_SPROC, [("id", id)]) [0] 
        customer = context.exec_param_sproc(context.GET_CUSTOMER_BY_EMAIL_SPROC, [("email", user.get("Email"))])[0]
        return customer.get("Id")

    def register(self, dictform):
        firstName = dictform.get("FirstName")
        lastName = dictform.get("LastName")
        dateOfBirth = dictform.get("DateOfBirth")
        phoneNumber = dictform.get("PhoneNumber")
        email = dictform.get("Email")
        password = dictform.get("Password")

        hashPassword = self.hash_password(password).decode()
        context.exec_param_sproc(context.ADD_CUSTOMER_SPROC, 
                                 [("firstName", str(firstName)),
                                  ("lastName", str(lastName)),
                                  ("dateOfBirth", dateOfBirth),
                                  ("phoneNumber", phoneNumber),
                                  ("email", email),
                                  ("password", hashPassword)])      
        return