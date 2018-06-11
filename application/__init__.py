from flask import Flask

from flask_restful import Api

app = Flask(__name__, instance_relative_config=True)

api = Api()

from application.resource.user_resource import RegisterApi

# add_resource function registers the routes with the framework using given endpoints
api.add_resource(RegisterApi,'/api/v1/auth/register')

api.init_app(app)

