import unittest
 
import os

from app.models import reviews

class ReviewTestCases(unittest.TestCase):
    """test cases for class review"""

    def setUp():
        """initialize app and define variables"""
        self.app = create_app(config_name = "testing")
        self.client = self.app.test_client()