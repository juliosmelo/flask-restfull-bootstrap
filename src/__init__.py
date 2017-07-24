from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
app.config.from_object(os.getenv('APP_CONFIG'))
db = SQLAlchemy(app)
api = Api(app)

from src.routes import *