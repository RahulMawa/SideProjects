####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.




class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"Account owned by: {self.owner} | Current Account Balance: {self.balance}."

    def deposit(self, d_amt):
        self.balance += d_amt
        print("Deposit Accepted!")

    def withdraw(self, w_amt):
        if self.balance >= w_amt:
            self.balance -= w_amt
            print("Withdrawal Accepted!")

        else:
            print("Withdrawal Rejected. Not enough funds!")


# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
acct1.owner




# 4. Show the account balance attribute
acct1.balance




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)



# ## Good job!
