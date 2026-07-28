import pytest
from practice.account import Account, SavingsAccount, CurrentsAccount

@pytest.fixture(scope="function")
def normal_account():
    print ("\t --> In Function Scope - Fixture!!!")
    return Account("A", 1000)

@pytest.fixture(scope="class")
def saving_account():
    print("\t --> In Class Scope - Fixture!!!")
    yield SavingsAccount("A",1000,5)

@pytest.fixture(scope="module")
def current_accout():
    print("\t --> In Module Scope - Fixture!!!")
    yield CurrentsAccount("A",1000,1000)
    print("\nTEARDOWN: cleaning up")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return{
        **browser_context_args,
        "viewport":{"width":1280,"height":720}, #for consistent window size
        "ignore_https_errors":True, #ParaBank sometimes has cert quirks
    }