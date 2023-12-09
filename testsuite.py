import unittest
from unittest_for_admin import TestAdmin
from unittest_for_client import TestClient
from unittest_for_investment import Test_investment as ti1
from unittest_for_manage_inv import Test_investment as ti2
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestAdmin('test_edit_client_password'))
    suite.addTest(TestAdmin('test_show_client_detail'))
    suite.addTest(TestClient('test_basic_operation'))
    suite.addTest(TestClient('test__information'))
    suite.addTest(ti1("test_calculate_fv"))
    suite.addTest(ti1("test_govnment_bond_coupon"))
    suite.addTest(ti1("test_calculate_mortgage"))
    suite.addTest(ti2("test_mortgage_initialization"))
    suite.addTest(ti2("test_zcb_initialization"))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()