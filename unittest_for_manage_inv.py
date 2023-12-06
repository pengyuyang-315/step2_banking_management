import unittest
from datetime import datetime
from bank_management.investment.investment import investment
from bank_management.investment.investment import mortgage
from bank_management.investment.investment import zero_coupon_bond
from bank_management.investment.investment import government_bond
from bank_management.investment.manage_investment import edit_rate,edit_risk,show_all_investment,recommendation_bond,mortgage_initialization,zcb_initialization



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
        self.mort_dict=mortgage_initialization()
        self.zcb_dict=zcb_initialization()
    def tearDown(self):
        print("tear down class")



    def test_mortgage_initialization(self):
        
        self.assertEqual("the monthly payment should be:  "+str(self.mort_dict[1].calculate_mortgage()),"the monthly payment should be:  5.0")
        self.assertEqual("the monthly payment should be:  "+str(self.mort_dict[2].calculate_mortgage()),"the monthly payment should be:  10.0")
        self.assertEqual("the monthly payment should be:  "+str(self.mort_dict[3].calculate_mortgage()),"the monthly payment should be:  16.666666666666668")
        self.assertEqual(self.mort_dict[3].rate,0.05)

    def test_zcb_initialization(self):
        self.assertEqual(pow((1+self.zcb_dict[1].rate),self.zcb_dict[1].n)*self.zcb_dict[1].pv,self.zcb_dict[1].calculate_fv())
        self.assertEqual(pow((1+self.zcb_dict[2].rate),self.zcb_dict[2].n)*self.zcb_dict[2].pv,self.zcb_dict[2].calculate_fv())
        self.assertEqual(self.zcb_dict[1].rate,0.03)
        self.assertEqual(self.zcb_dict[2].rate,0.06)
        
        
   
        
unittest.main(argv=[''], verbosity=3, exit=False)