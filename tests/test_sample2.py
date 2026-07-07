#def test_additon():
#	result = 2+3
#	assert result == 7 #assert is the keyword which determine if the test case is pass or fail

#LEARNING MORE ABOUT FIXTURE SCOPE

import pytest

@pytest.fixture(scope="function")
def function_fixture():
    print("\nIn Function Fixture")
    return 1

@pytest.fixture(scope="module")
def module_fixture():
    print("\nIn Module Fixture")
    return 1

def test_one(function_fixture):
    print("In test One")
    
def test_two(function_fixture):
    print("In test two")


def test_three(module_fixture):
    print("In test three")

def test_four(module_fixture):
    print("In test four")    