import pytest
from PageObject.login_page import LoginPage
from Utils.excel_reader import get_test_data

test_data = get_test_data("TestData/TestData.xlsx", "ValidUserLogin")


@pytest.mark.parametrize("data", test_data)
def test_valid_user_login(page, data):
    """ This test is to check if username or password is correct
        system should go to inventory page"""

    login_page = LoginPage(page)

    login_page.login(data['username'], data['password'])

    assert "inventory" in page.url, "Login failed"
