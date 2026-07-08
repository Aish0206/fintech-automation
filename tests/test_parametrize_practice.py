import pytest
from practice.account import Account


# ---------------- Deposit Test Data ----------------

@pytest.mark.parametrize(
    "deposit_amount, expected_balance",
    [
        (100, 1100),
        (200, 1200),
        (1, 1001),
        (9999, 10999),
    ]
)
@pytest.mark.regression
def test_deposit(normal_account, deposit_amount, expected_balance):
    normal_account.deposit(deposit_amount)
    assert normal_account.balance == expected_balance


@pytest.mark.parametrize(
    "bad_amount, message",
    [
        (0, "Deposit cannot be zero"),
        (-100, "Deposit cannot be negative"),
    ]
)
@pytest.mark.regression
def test_deposit_negative(normal_account, bad_amount, message):
    with pytest.raises(ValueError, match=message):
        normal_account.deposit(bad_amount)

    assert normal_account.balance == 1000


# ---------------- Withdraw Test Data ----------------

@pytest.mark.parametrize(
    "withdraw_amount, balance_left",
    [
        (300, 700),
        (1000, 0),
        (7.5, 992.5),
        (0.1, 999.9),
    ]
)
def test_withdraw(normal_account, withdraw_amount, balance_left):
    normal_account.withdraw(withdraw_amount)
    assert normal_account.balance == balance_left


@pytest.mark.parametrize(
    "bad_withdraw_amount, withdraw_message",
    [
        (0, "Withdraw amount can not be zero"),
        (1001, "Insufficient balance"),
        (-100, "Withdraw amount can not be negative"),
        (-0.1, "Withdraw amount can not be negative"),
        (1000.1, "Insufficient balance"),
    ]
)
def test_withdraw_negative(
    normal_account,
    bad_withdraw_amount,
    withdraw_message,
):
    with pytest.raises(ValueError, match=withdraw_message):
        normal_account.withdraw(bad_withdraw_amount)

    assert normal_account.balance == 1000


# ---------------- Account Details ----------------

@pytest.mark.smoke
def test_account_details(normal_account):
    assert normal_account.owner == "A"
    assert normal_account.balance == 1000