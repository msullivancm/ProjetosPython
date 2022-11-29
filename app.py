from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hoteis(Resource):
    def get(self):
        return {'hoteis': 'Meus Hoteis'}
    
    def set(self):
        pass

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)