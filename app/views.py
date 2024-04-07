from flask_restx import Resource, Api
from app import api

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}