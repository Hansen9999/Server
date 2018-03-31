from flask_restful import Resource
from flask import request
import json

from api.models.customer import Customer
from api import session

import timeit
import sys

class SignUp(Resource):
    
    # define the POST method
    def post(self):
        json_user_data = request.data
        user_data = json.loads(json_user_data)

        try:
            username = user_data['username']
            password = user_data['password']
        except:
            return {"status": 1, "message": "invalid format"}
        
        try:
            new_customer = Customer(username, password)
            session.add(new_customer)
            session.flush()
            session.commit()
        except:
            return {"status": 1, "message": "error adding data to database"} 

        return {"status": 0, "message": "sign up success"}