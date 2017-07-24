from src import db
from flask_restful import Resource
from flask_restful import reqparse
from marshmallow import Schema, fields
from src.models.model import MyAwesomeModel


parser = reqparse.RequestParser()
parser.add_argument('parameter')


class AwesomeSerializer(Schema):
    """
        AwesomeSerializer
    """
    latitude = fields.Str()
    longitude = fields.Str()


class AwesomeResource(Resource):
    """
        Controloador de AwesomeResource
    """
    serializer = AwesomeSerializer()
    def get(self):
        awesome = MyAwesomeModel.query.all()
        serializer = MyAwesomeModelSerializer(many=True)
        return serializer.dump(awesome).data, 200

    def post(self):
        args = parser.parse_args()
        model_instace = MyAwesomeModel(args['latitude'], args['longitude'])
        model.save()
        serializer = self.serializer
        return serializer.dump(model_instace).data, 201
