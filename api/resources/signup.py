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
        print(json_user_data.decode('utf-8'))
        user_data = json.loads(json_user_data.decode('utf-8'))

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
        except Exception as e:
            print(e)
            return {"status": 2, "message": "error adding data to database"} 

        return {"status": 0, "message": "sign up success"}
