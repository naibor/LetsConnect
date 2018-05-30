import unittest 

import os

from app.models import users

class UsersTestCases (unittest.TestCase):
    """class for user test case"""

    def setUp(self):
        """initialize app and defines variables"""
        self.app = create_app(config_name = "testing")
        self.client = self.app.test_client()