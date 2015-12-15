__author__ = 'alan'
import re


class Account(object):

    def __init__(self, accname, ccnum, cclimit):
        self.accname = accname
        self._ccnum = self._ver_cc_num(ccnum)
        self._cclimit = self._cln_amt(cclimit)
        self.accbalance = 0


    @property
    def ccnum(self):
        return self._ccnum


    @ccnum.setter
    def ccnum(self, ccnum):
        self._ccnum = self._ver_cc_num(ccnum)


    @property
    def cclimit(self):
        return self._cclimit


    @cclimit.setter
    def cclimit(self, cclimit):
        self._cclimit = self._cln_amt(cclimit)


    def charge_acc(self, chrgamt):
        """
        This method is meant to charge an account with a valid credit card number.
        :param chrgamt: is an integer that is used to place a charge value on the account:
        :return True if the charge was successfully added. False if it was declined:
        """
        if self.ccnum != 'error':
            chrgamt = self._cln_amt(chrgamt)
            if self.accbalance + chrgamt <= self.cclimit:
                self.accbalance += chrgamt
                return True
            else:
                return False
        else:
            return False


    def credit_acc(self, crdamt):
        """
        This method is meant to credit an account with a valid credit card number
        :param crdamt: is an integer that is used to place a credit value on the account:
        :return True if a credit was successfully added. False if it was declined:
        """
        if self.ccnum != 'error':
            crdamt = self._cln_amt(crdamt)
            self.accbalance -= crdamt
            return True
        else:
            return False


    def _ver_cc_num(self, ccnum):
        """
        This method uses the Luhn 10 algorithm to check for incorrectly entered credit card numbers
        :param ccnum: should be an integer:
        :return If true, return validated credit card number.If false, return error:
        """
        ccnumarry = [int(x) for x in str(ccnum)]
        ccnumarry.reverse()
        oddccnums = sum([val for ind, val in enumerate(ccnumarry) if (ind + 1) % 2 != 0])
        evenccnums = [2 * val for ind, val in enumerate(ccnumarry) if (ind + 1) % 2 == 0]
        evenccnums = sum([ 1 + (x % 10) if x > 9 else x for x in evenccnums])
        check = oddccnums + evenccnums
        if check % 10 == 0:
            return int(ccnum)
        else:
            return 'error'


    def _cln_amt(self, amt):
        """
        Remove all non integers from value string and convert that string value into an integer
        :param amt: is the string value:
        :return amt as an integer without any symbols:
        """
        amt = re.sub(r'[^\d]', '', str(amt))
        return int(amt)