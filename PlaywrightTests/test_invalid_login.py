import pytest
from PageObject.login_page import LoginPage
from Utils.excel_reader import get_test_data

test_data = get_test_data("TestData/TestData.xlsx", "InvalidUserLogin")


@pytest.mark.parametrize("data",test_data)
def test_invalid_user_login(page, data):
    """ This test is to check if username or password is invalid or missing
    system should throw error msg correctly"""

    login_page = LoginPage(page)

    login_page.login(data['username'], data['password'])

    error_message = login_page.get_error_message()

    assert 'Epic sadface' in error_message
