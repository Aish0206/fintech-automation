class Account: #1. CLASS: Blueprint
	def __init__(self, owner, balance): #2.__init__: run when you create one
		self.owner = owner	#3. self + ATTRIBUTES: data this account holds
		self.balance = balance

	def deposit(self,amount): # 4. METHOD: an action the account can do
		self.balance = self.balance + amount
		print("Your account is credit with Rs."+str(amount))
		print("Your have Rs." + str(self.balance) +" in your account")

	def withdraw(self, amount):
		if amount> self.balance:
			print("Insufficient balance")
		else:
			self.balance = self.balance - amount
			print ("Your account now have Rs." + str(self.balance)+" left")

	def check_balance(self):
		print("Your account have Rs." + str(self.balance))


#using the blueprint to make a real account (an "object" or an "instance")
acc = Account("Aishwary", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()