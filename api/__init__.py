import flask
import flask_restless
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.schema import CreateTable
from sqlalchemy import *
from flask_cors import CORS
from flask_restful import Api

app = flask.Flask(__name__)
api = Api(app)

# Create our SQLAlchemy DB engine
engine = create_engine('mysql+mysqlconnector://root:Wo.shidashuaige1'
                       + '@localhost:3306/CS329E')
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = scoped_session(Session)

Base = declarative_base()
Base.metadata.bind = engine

# Import all models to add them to Base.metadata
from api.models.customer import Customer

Base.metadata.create_all()

print('Table Schema: ')
print(CreateTable(Customer.__table__).compile(engine))

manager = flask_restless.APIManager(app, session=session)

# Load Resources
from api.resources.login import Login
from api.resources.signup import SignUp
api.add_resource(Login, '/login')
api.add_resource(SignUp, '/signup')

cors = CORS(app, resources={r"/*": {"origins": "*"}})
