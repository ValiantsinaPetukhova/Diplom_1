import pytest
from practikum.burger import Burger
from practikum.database import Database


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def database():
    database = Database()
    return database




