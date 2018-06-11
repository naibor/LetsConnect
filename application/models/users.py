USERSINFO = {}
class User():
    count = 0
    # track user count
    def __init__(self, name, username, email, password, confirmpassword):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.confirmpassword = confirmpassword
        User.count += 1 #increments by 1 with every user


    def save(self):
        """users are added and saved"""
        new_user = {
            "name":self.name,
            "username":self.username,
            "email":self.email,
            "password":self.password,
            "confirmpassword":self.confirmpassword
        }

        USERSINFO[self.name]=new_user

    


