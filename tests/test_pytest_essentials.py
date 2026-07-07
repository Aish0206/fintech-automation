import pytest
from practice.account import Account, SavingsAccount, CurrentsAccount

class TestAccount:
    
    def test_account_details(self, normal_account):
        #acc = Account("A", 1000)
        
        #assert acc.balance == 1000
        #assert acc.owner == "A"
        assert normal_account.balance == 1000
        assert normal_account.owner == "A"

    def test_deposit_successful(self, normal_account):
        #acc1 = Account("A", 1000)

        #acc1.deposit(200)
        #assert acc1.balance == 1200

        normal_account.deposit(200)  
        assert normal_account.balance == 1200

    def test_deposit_negative(self,normal_account):
        
        #acc2 = Account("B", 700)
        #acc3 = Account("C", 200)
        with pytest.raises(ValueError, match="Deposit cannot be zero"):
            #acc2.deposit(0)
            normal_account.deposit(0)

        #assert acc2.balance == 700
        normal_account.balance == 1000
             
        with pytest.raises(ValueError, match="Deposit cannot be negative"):
            #acc3.deposit(-100)
            normal_account.deposit(-100)
        #assert acc3.balance == 2004
        assert normal_account.balance == 1000
         
    def test_withdraw(self,normal_account):   
        #acc1 = Account("A", 1000)

        #acc1.withdraw(200) 
        normal_account.withdraw(200) 
        #assert acc1.balance == 800
        assert normal_account.balance == 800

    def test_withdraw_negative(self,normal_account):
        #acc1 = Account("A", 1000)
        #acc2 = Account("B", 700)
        #acc3 = Account("C", 200)

        with pytest.raises(ValueError, match="Withdraw amount can not be zero"):
            normal_account.withdraw(0)
        assert normal_account.balance == 1000
             
        with pytest.raises(ValueError, match="Withdraw amount can not be negative"):
            normal_account.withdraw(-100)
        assert normal_account.balance == 1000

        with pytest.raises(ValueError, match="Insufficient balance"):
            normal_account.withdraw(1001)
        assert normal_account.balance == 1000
    
    def test_check_balance(self):
        acc1 = Account("A",0)
        assert acc1.balance == 0

        with pytest.raises(ValueError, match= "Balance cannot be negative"):
            acc2 = Account ("B", -100)

        acc3 = Account("C", 7.5)
        assert acc3.balance == 7.5

    def test_saving_account(self,saving_account):
        #acc1 = SavingsAccount("A", 1000, 2)
        saving_account.add_interest()

        assert saving_account.balance == 1050

    def test_current_account(self,current_accout,capsys):
        #acc1 = CurrentsAccount("A",1000,1000)
        current_accout.update_current_account_balance()

        assert current_accout.balance == 2000

        current_accout.check_balance()
        capture = capsys.readouterr()

        assert capture.out == "A's account have Rs.2000 (including overdraft limits)\n"