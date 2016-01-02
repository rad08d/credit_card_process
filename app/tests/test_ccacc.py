__author__ = 'alan'
import unittest
from app.ccacc.account import Account


class TestCCProcModule(unittest.TestCase):

    def test_create_acc(self):
        acc = Account(name='Alan', ccnum='946546', cclimit='$3000')


    def test_cln_amt(self):
       acc = Account(name='Alan', ccnum='5454545454545454',cclimit='$3000')
       self.assertEqual(acc._cln_amt('$10000'), 10000)


    def test_update_cclimit(self):
       acc = Account(name='Alan', ccnum='5454545454545454',cclimit='$300')
       acc.cclimit = '$850'
       self.assertEqual(850, acc.cclimit)


    def test_verify_acc_cc_num_change_valid(self):
       acc = Account(name='Alan', ccnum='5454545454545454',cclimit='$3000')
       acc.ccnum = '4111111111111111'
       self.assertEqual(4111111111111111, acc.ccnum)


    def test_verify_acc_cc_num_change_invalid(self):
       acc = Account(name='Alan', ccnum='5454545454545454',cclimit=3000)
       acc.ccnum = '4111111111111112'
       self.assertEqual(False, acc.ccnum)


    def test_charge_acc_accepted(self):
        acc = Account(name='Alan', ccnum='4111111111111111', cclimit='$3000')
        self.assertTrue(acc.charge_acc('$3000'))


    def test_charge_acc_declined(self):
        acc = Account(name='Alan', ccnum=4111111111111111,cclimit='$3000')
        self.assertFalse(acc.charge_acc('$3500'))


    def test_charge_acc_success_then_decline(self):
        acc = Account(name='Alan', ccnum='4111111111111111',cclimit='$1000')
        self.assertTrue(acc.charge_acc('$300'))
        self.assertFalse(acc.charge_acc('$2701'))


    def test_credit_acc_above_zero(self):
        chrgamt = '$2589'
        crdamt = '$50'
        acc = Account(name='Alan', ccnum='4111111111111111',cclimit='$3000')
        acc.charge_acc(chrgamt)
        acc.credit_acc(crdamt)
        self.assertEqual(acc.balance, 2539)


    def test_credit_acc_below_zero(self):
        chrgamt = '$2589'
        crdamt = '$2600'
        acc = Account(name='Alan', ccnum='4111111111111111',cclimit='$3000')
        acc.charge_acc(chrgamt)
        acc.credit_acc(crdamt)
        self.assertEqual(acc.balance, -11)


    def test_verify_acc_cc_num(self):
        acc = Account(name='Alan', ccnum='5454545454545454',cclimit='$3000')
        self.assertEqual(5454545454545454, acc.ccnum)


    def test_verify_acc_cc_num_error(self):
        acc = Account(name='Alan', ccnum='1234567890123456',cclimit='$3000')
        self.assertEqual(False, acc.ccnum)


    def test_charge_acc_decline_invalid_cc_num(self):
        acc = Account(name='Alan', ccnum='1234567890123456',cclimit='$3000')
        self.assertFalse(acc.charge_acc('$59'))


    def test_credit_acc_decline_invalid_cc_num(self):
        acc = Account(name='Alan', ccnum='1234567890123456',cclimit='$3000')
        self.assertFalse(acc.credit_acc('$59'))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCCProcModule)
    unittest.TextTestRunner(verbosity=2).run(suite)