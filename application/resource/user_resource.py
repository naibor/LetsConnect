
New_user(User)

class UserAPI(Resource):
    decorators = [auth,login_required]
    def __init__(self):
        




    def get(self, id):
        pass

    def put(self, id):
        pass

    
    def delete(self, id):
        pass





api.add_resource(UserAPI,'/api/v1/auth/register')
# add_resource function registers the routes with the framework using given endpoints


