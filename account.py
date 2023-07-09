class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f'owner name is:{self.owner}\nyour current account balance is:{self.balance} '
    def dep_bal(self,dep_bal):
        self.balance=self.balance+dep_bal
        print('money credited')
    def wid_bal(self,wid_bal):
        if self.balance>wid_bal:
            self.balance=self.balance-wid_bal
            print ('money withdraw')
        else:
            return 'your withdraw money is less then your bank balance'
acc=Account('sam',200)
print(acc)
print(acc.wid_bal(100))

print(acc.dep_bal(500))
print(acc.balance)
print(acc.dep_bal(100))
