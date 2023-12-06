import unittest
from datetime import datetime
from bank_management.investment.investment import investment
from bank_management.investment.investment import mortgage
from bank_management.investment.investment import zero_coupon_bond
from bank_management.investment.investment import government_bond


class Test_investment(unittest.TestCase):
    def setUp(self):
        self.invst=investment(0.05,2)
        self.mort1=mortgage(0.05,5,10,2000)
        self.mort2=mortgage(0.06,5,10,2000)
        self.mort3=mortgage(0.07,5,10,2000)
        self.mort4=mortgage(0.08,5,10,2000)
        self.zcb1=zero_coupon_bond(0.04,5,2000,10)
        self.zcb2=zero_coupon_bond(0.05,5,2000,10)
        self.zcb3=zero_coupon_bond(0.05,7,2000,10)
        self.zcb4=zero_coupon_bond(0.05,10,2000,10)
        self.gov1=government_bond(0.05,5,2000,10,2)
        self.gov2=government_bond(0.04,5,2000,10,2)
        self.gov3=government_bond(0.03,5,2000,10,2)
        self.gov4=government_bond(0.05,10,2000,10,1)
    def tearDown(self):
        print("tear down class")

    def test_calculate_mortgage(self):
        
        self.assertEqual("the monthly payment should be:  "+str(self.mort1.calculate_mortgage()),"the monthly payment should be:  8.333333333333334")
        self.assertEqual("the monthly payment should be:  "+str(self.mort2.calculate_mortgage()),"the monthly payment should be:  10.0")
        self.assertEqual("the monthly payment should be:  "+str(self.mort3.calculate_mortgage()),"the monthly payment should be:  11.666666666666668")
        self.assertEqual("the monthly payment should be:  "+str(self.mort4.calculate_mortgage()),"the monthly payment should be:  13.333333333333332")

    def test_calculate_fv(self):
        
        self.assertEqual(pow((1+self.zcb1.rate),self.zcb1.n)*self.zcb1.pv,self.zcb1.calculate_fv())
        self.assertEqual(pow((1+self.zcb2.rate),self.zcb2.n)*self.zcb2.pv,self.zcb2.calculate_fv())
        self.assertEqual(pow((1+self.zcb3.rate),self.zcb3.n)*self.zcb3.pv,self.zcb3.calculate_fv())
        self.assertEqual(pow((1+self.zcb4.rate),self.zcb4.n)*self.zcb4.pv,self.zcb4.calculate_fv())

    def test_govnment_bond_coupon(self):
        self.assertEqual(self.gov1.pv*self.gov1.rate/2,self.gov1.calculate_coupon())
        self.assertEqual(self.gov2.pv*self.gov2.rate/2,self.gov2.calculate_coupon())
        self.assertEqual(self.gov3.pv*self.gov3.rate/2,self.gov3.calculate_coupon())
        self.assertEqual(self.gov4.pv*self.gov4.rate,self.gov4.calculate_coupon())

        
unittest.main(argv=[''], verbosity=3, exit=False)