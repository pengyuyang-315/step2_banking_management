import unittest
from datetime import datetime
from bank_management.user.client import client
class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        cls.transfer_amount = 200.0
        # Initialize common values for all test cases
        # cls.client1 = client("Alice", "alice@email.com", "123456789", 1000.0, 1234)
        # cls.client2 = client("Bob", "bob@email.com", "987654321", 500.0, 5678)

    @classmethod
    def tearDownClass(cls):
        # Clean up common resources
        print('tearDownClass')

    def setUp(self):
        print("setUp")
        # Initialize values specific to each test case
        
        self.client1 = client("Alice", "alice@email.com", "123456789", 1000.0, 1234)
        self.client2 = client("Bob", "bob@email.com", "987654321", 500.0, 5678)

    def tearDown(self):
        # Clean up resources used in the test case
        print("tearDown")

    def test_basic_operation(self):
        print("run test_save_money")
        self.client1.save_money(500.0)
        self.assertEqual(self.client1._balance, 1500.0)
        print("run test_withdraw_money")
        self.client2.withdraw_money(200.0)
        self.assertEqual(self.client2._balance, 300.0)
        print("run test_transfer")
        self.client1.transfer(self.transfer_amount, self.client2)
        self.assertEqual(self.client1._balance, 1300.0)
        self.assertEqual(self.client2._balance, 500.0)

    def test__information(self):
        info = self.client1.show_information()
        self.assertEqual(info[0], "Alice")
        self.assertEqual(info[4], 1000.0)
        self.assertEqual(self.client1.get_password(),1234)

if __name__ == '__main__':
    unittest.main()
