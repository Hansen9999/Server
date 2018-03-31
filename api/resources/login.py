from flask_restful import Resource
from flask import request
import json

from api.models.customer import Customer
from api import session

import timeit
import sys

class Login(Resource):

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
            customer_query = session.query(Customer).filter(Customer.name == username)
            if customer_query.count() < 1:
                return {"status": 2, "message": "user " + username + " doesn't exist"}
            
            customer = customer_query.first()
            if password != customer.password:
                return {"status": 3, "message": "invalid password"}

        except:
            return {"status": 4, "message": "error reading data from database"} 

        return {"status": 0, "message": "login success"}