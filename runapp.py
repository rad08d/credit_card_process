__author__ = 'alan'
import fileinput
from app.ccacc.account import Account

def main():
    """
    Process all command line arguments. Print out the balances of all accounts after processing.
    """
    accdict = {}
    for line in fileinput.input():
        process_input(line, accdict)
    fileinput.close()
    alphasort = sorted([k for k in accdict.iterkeys()])
    for name in alphasort:
        print accdict[name].name + ':', '$' + str(accdict[name].accbalance) if accdict[name].ccnum != 'error' else accdict[name].ccnum


def process_input(input, accdict):
    """
    Process all arguments into accounts and add them to the dictionary. Return a dictionary of all active accounts.
    :param input: the command line arguments converted into a list:
    :param accdict: a dictionary containing all active accounts with the account name as a key.
    :return an updated accdict:
    """
    accinfo = input.split()
    if accinfo[1] in accdict:
        acc = accdict[accinfo[1]]
    else:
        acc = None
    if not acc and accinfo[0] == 'Add':
        acc = Account(name=accinfo[1], ccnum=accinfo[2], cclimit=accinfo[3])
    if acc and accinfo[0] == 'Charge':
        acc.charge_acc(accinfo[2])
    if acc and accinfo[0] == 'Credit':
        acc.credit_acc(accinfo[2])
    accdict[acc.name] = acc
    return accdict


if __name__ == '__main__':
    main()