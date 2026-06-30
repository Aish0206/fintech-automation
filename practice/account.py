class Account: #1. CLASS: Blueprint
	def __init__(self, owner, balance): #2.__init__: run when you create one
		self.owner = owner	#3. self + ATTRIBUTES: data this account holds
		self.balance = balance

	def deposit(self,amount): # 4. METHOD: an action the account can do
		self.balance = self.balance + amount
		print(self.owner + "'s account is credit with Rs."+str(amount))
		print(self.owner +" have Rs." + str(self.balance) +" in your account")

	def withdraw(self, amount):
		if amount> self.balance:
			print("Insufficient balance")
		else:
			self.balance = self.balance - amount
			print (self.owner +"'s account now have Rs." + str(self.balance)+" left")

	def check_balance(self):
		print(self.owner + "'s account have Rs." + str(self.balance))

class SavingsAccount(Account): #SavingsAccount is inherited from Account class
	def __init__(self,owner, balance, interest_rate):
		super().__init__(owner,balance) 	#reusing Account's setup for owner & balance attributes
		self.interest_rate = interest_rate
	def add_interest(self):
		interest = self.balance * self.interest_rate/ 100
		self.balance = self.balance + interest
		print(self.owner + " have got interest of Rs."+ str(interest) +" and his/her current balance is Rs."+ str(self.balance))

class CurrentsAccount(Account): #CurrentsAccount is inherits from Account (parent/super) class
	def __init__(self,owner, balance, overdraft_limit):
		super().__init__(owner,balance) 
		self.overdraft_limit = overdraft_limit

	def update_current_account_balance(self):
		self.balance = self.balance + self.overdraft_limit

	def check_balance(self):
		print(self.owner + "'s account have Rs." + str(self.balance)+" (including overdraft limits)")

#using the blueprint to make a real account (an "object" or an "instance")
acc = Account("Aishwary", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

sav_acc = SavingsAccount("Pratiksha", 1000, 5)
sav_acc.deposit(2500)
sav_acc.withdraw(300)
sav_acc.add_interest()
sav_acc.check_balance()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

cur_acc = CurrentsAccount("Om", 2000, 1000)
cur_acc.update_current_account_balance()

cur_acc.deposit(500)
cur_acc.check_balance()
cur_acc.withdraw(3000)
cur_acc.check_balance()