import unittest
import os
import json
from app.models import business

class BusinessTestCase(unittest.TestCase):
    """class for business testcases """

    def setUp(self):
        """initialize app and define test variables"""
        self.app = create_app(config_name = "testing")
        self.client = self.app.test_client
        