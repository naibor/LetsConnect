import unittest 

import os

from app.models import users

class RegisterApiTestCases (unittest.TestCase):
    """class for tegister user test case"""

    def setUp(self):
        """initialize app and defines variables"""
        self.app = create_app(config_name = "testing")
        self.client = self.app.test_client()
        self.usersinfo ={
                      name:"Lisa",
                      username:"naibor",
                      email:"liznaibor@gmail.com",
                      password:"12365",
                      confirm_password:"12365"
                      }

    def test_register_api(self):
        response = self.client().post('/api/v1/auth/register, data = self.usersinfo)
        self.assertEqual(response.status_code,201)
        self.assertIn("Lisa",str(response.data))

