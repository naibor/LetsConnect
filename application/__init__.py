from flask import Flask

from flask_restful import Api

app = Flask(application)

api = Api(app)