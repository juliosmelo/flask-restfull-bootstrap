# importar resources aqui
from src import api
from src.resources.awesome_resource import AwesomeResource
api.add_resource AwesomeResource, '/')
