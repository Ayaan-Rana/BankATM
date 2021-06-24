class ATM(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def balanceEnquiry(self):
        print('Balance of your account: ')

    def cashWithdrawal(self):
        print('Enter amount needed to withraw: ')