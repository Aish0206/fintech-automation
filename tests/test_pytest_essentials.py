import pytest
from practice.account import Account
from practice.account import SavingsAccount
from practice.account import CurrentsAccount

class TestAccount:
    
    def test_account_details(self):
        acc = Account("A", 1000)
        
        assert acc.balance == 1000
        assert acc.owner == "A"

    def test_deposit_successful(self):
        acc1 = Account("A", 1000)

        acc1.deposit(200)  
        assert acc1.balance == 1200

    def test_deposit_negative(self):
        
        acc2 = Account("B", 700)
        acc3 = Account("C", 200)
        with pytest.raises(ValueError, match="Deposit cannot be zero"):
            acc2.deposit(0)
            assert acc2.balance == 700
             
        with pytest.raises(ValueError, match="Deposit cannot be negative"):
            acc3.deposit(-100)
            assert acc3.balance == 200
         
    def test_withdraw(self):   
        acc1 = Account("A", 1000)

        acc1.withdraw(200)  
        assert acc1.balance == 800

    def test_withdraw_negative(self):
        acc1 = Account("A", 1000)
        acc2 = Account("B", 700)
        acc3 = Account("C", 200)

        with pytest.raises(ValueError, match="Withdraw amount can not be zero"):
            acc2.withdraw(0)
            assert acc2.balance == 700
             
        with pytest.raises(ValueError, match="Withdraw amount can not be negative"):
            acc3.withdraw(-100)
            assert acc3.balance == 200

        with pytest.raises(ValueError, match="Insufficient balance"):
            acc1.withdraw(1001)
            assert acc1.balance == 1000
    
    def test_check_balance(self):
        acc1 = Account("A",0)
        assert acc1.balance == 0

        with pytest.raises(ValueError, match= "Balance cannot be negative"):
            acc2 = Account ("B", -100)

        acc3 = Account("C", 7.5)
        assert acc3.balance == 7.5

    def test_saving_account(self):
        acc1 = SavingsAccount("A", 1000, 2)
        acc1.add_interest()

        assert acc1.balance == 1020

    def test_current_account(self,capsys):
        acc1 = CurrentsAccount("A",1000,1000)
        acc1.update_current_account_balance()

        assert acc1.balance == 2000

        acc1.check_balance()
        capture = capsys.readouterr()

        assert capture.out == "A's account have Rs.2000 (including overdraft limits)\n"