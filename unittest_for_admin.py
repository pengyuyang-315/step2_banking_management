import unittest
from datetime import datetime
from bank_management.user.client import client
from bank_management.user.admin import admin, admin_login,admin_operations

class TestAdmin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up common resources for the entire test class
        cls.admin1 = admin("John", 123, 456)
        cls.client1 = client("Alice", "alice@email.com", 123456789, 1000.0, 1234)
        cls.clients_dict = {"Alice": cls.client1}

    @classmethod
    def tearDownClass(cls):
        # Clean up common resources for the entire test class
        print("tearDownClass")

    def setUp(self):
        self.operationNumber1 = 1
        self.operationNumber2 = 2
        self.operationNumber3 = 3
        self.new_one = 1234
        # Set up resources specific to each test case
        print("setUp")

    def tearDown(self):
        # Clean up resources used in each test case
        print("tearDown")

    def test_edit_client_password(self):
        print("test_edit_client_password")
        self.admin1.edit_client_detail(self.client1,self.operationNumber1,self.new_one)
        self.assertEqual(self.client1._password, 1234)

    def test_show_client_detail(self):
        # Test the show_client_detail method of the admin class
        print("test_show_client_detail")
        information = self.admin1.show_client_detail(self.client1)
        self.assertEqual(information, self.client1.show_information())

    def test_edit_client_phoneNumber(self):
        print("test_edit_client_phoneNumber")
        self.admin1.edit_client_detail(self.client1,self.operationNumber2,self.new_one)
        self.assertEqual(self.client1.phoneNumber, 1234)

    def test_edit_client_emai(self):
        print("test_edit_client_email")
        self.admin1.edit_client_detail(self.client1,self.operationNumber3,self.new_one)
        self.assertEqual(self.client1.email, 1234)

    
if __name__ == '__main__':
    unittest.main()
