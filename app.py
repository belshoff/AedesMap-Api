from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.location import Location

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Location, '/location')

if __name__ == '__main__':
    app.run(debug=True)