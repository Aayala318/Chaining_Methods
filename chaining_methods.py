# Create a file with the User class, including the __init__ and make_deposit methods
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = 0

    def makeDeposit(self, amount):
        self.account += amount
        return self

# Add a make_withdrawal method to the User class
    def makeWithdrawl(self, amount):
        self.account -= amount
        return self

# Add a display_user_balance method to the User class
    def displayUserBalance(self):
        print(f'User: {self.name}, Balance: ${self.account}')
        return self
    
    def transferMoney(self, otherUser, amount):
        otherUser.makeDeposit(amount)
        self.makeWithdrawl(amount)
        print('\n')
        return self

# Create 3 instances of the User class
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
denisse = User('Denisse', 'djlove@1.com')
denisse.makeDeposit(10).makeDeposit(5).makeDeposit(2).makeWithdrawl(3).displayUserBalance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
jojo = User('Jojo', 'jham@23.com')
jojo.makeDeposit(20).makeDeposit(30).makeWithdrawl(10).makeWithdrawl(40).displayUserBalance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
abby = User('Abby', 'abby@ham.com')
abby.makeDeposit(300).makeWithdrawl(15).makeWithdrawl(50).makeWithdrawl(150).displayUserBalance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
abby.transferMoney(jojo,20).displayUserBalance()
jojo.displayUserBalance()