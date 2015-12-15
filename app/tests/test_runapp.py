__author__ = 'alan'
import unittest

import runapp
from app.ccacc.account import Account


class TestRunApp(unittest.TestCase):

    def test_process_input_create_acc(self):
        dict = {}
        dict = runapp.process_input('Add Tom 4111111111111111 $1000', dict)
        self.assertEqual(dict['Tom'].accname, 'Tom')
        self.assertEqual(dict['Tom'].ccnum, 4111111111111111)
        self.assertEqual(dict['Tom'].cclimit, 1000)


    def test_process_input_charge_acc(self):
        dict = {}
        acc = Account(accname='Tom', ccnum='4111111111111111', cclimit='$1000')
        dict[acc.accname] = acc
        dict = runapp.process_input('Charge Tom $500',dict)
        self.assertEqual(dict[acc.accname].accname, 'Tom')
        self.assertEqual(dict[acc.accname].ccnum, 4111111111111111)
        self.assertEqual(dict[acc.accname].cclimit, 1000)
        self.assertEqual(dict[acc.accname].accbalance, 500)



    def test_process_input_credit_acc(self):
        dict = {}
        acc =  Account(accname='Tom', ccnum='4111111111111111', cclimit='$1000')
        acc.charge_acc('$800')
        dict[acc.accname] = acc
        accarry = runapp.process_input('Credit Tom $500',dict)
        self.assertEqual(dict[acc.accname].accname, 'Tom')
        self.assertEqual(dict[acc.accname].ccnum, 4111111111111111)
        self.assertEqual(dict[acc.accname].cclimit, 1000)
        self.assertEqual(dict[acc.accname].accbalance, 300)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRunApp)
    unittest.TextTestRunner(verbosity=2).run(suite)