from flask_restful import Resource

from api.models.customer import Customer
from api import session

import timeit
import sys

class Login(Resource):

    # define the GET method
    def get(self):
        
        return {"status": 1, "message": "login success"}