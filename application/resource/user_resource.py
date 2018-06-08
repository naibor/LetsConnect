from flask import Flask
from flask-restful import resource
from application.models.users import User, usersinfo
from marshmallow import schema, fields
import datetime 
from application import app, api


A_user=User("lisa","naibor","liznaibor@gmail.com","12365","12365")
usersinfo ={name:{
    name:"lisa",
    username:"naibor",
    email:"liznaibor@gmail.com",
    password:"12365",
    confirm_password:"12365"
},
{   name:"Lala",
    username:"bure",
    email:"naibor@gmail.com",
    password:"1236",
    confirm_password:"1236"

}}
class RegisterSchema(schema):
    class Meta:
        fields =  ("name","username","email","password", "confirm_password", "date_created")
        # tuple or list of fields to be included in the serialized results
        exclude = ("password","confirmpassword","date_created")
        # what to exclude from serialized results nested lists in dotted delimiter
        ordered = True
        # order the output to an collections.OrderedDict

schema = RegisterSchema()
data = schema.dumps(A_user)  
# dump serializes an object to 
# native data type according to schema's fields
# to return json string  

class RegisterApi(Resource):
    def __init__(self, name, username, email,password,confim_password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.date_created = datetime.now()

    def post(self):
        """register user"""
        # get post data in json
        postscheme = RegisterSchema()
        data = postscheme.dumps(A_user)
        import pdb; pdb,set_trace()
        data.save()
        return {'data':"you are registered"},201

class LogInApi():
    def __init__(self):
        pass
    def post():
        pass

class LogOutApi():
    def __init__():
        pass

    def post():
        pass
class ResetPasswordApi():
    def __init__():
        pass

    def post():
        pass


# add_resource function registers the routes with the framework using given endpoints
api.add_resource(RegisterApi,'/api/v1/auth/register')
api.add_resource(LogInApi, '/api/v1/auth/login')
api.add_resource(LogOutApi, '/api/v1/auth/logout')
api.add_resource(ResetPasswordApi, '/api/v1/auth/reset-password')


