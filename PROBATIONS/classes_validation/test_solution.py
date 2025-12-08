import sys
print('sys.path', sys.path)
import pytest
from validate import validate_form
from repository import users
from errors import InvalidEmailError, PasswordsNotMatchError, UserExistsError


@pytest.fixture()
def user_form():
    return {
        'name': 'John42',
        'email': 'john42@mail.com',
        'password': 'password123',
        'password_confirmation': 'password123'
    }


def test_form_is_valid(user_form):
    assert validate_form(user_form) is True


def test_invalid_email(user_form):
    user_form['email'] = 'invalid-email'
    with pytest.raises(InvalidEmailError):
        validate_form(user_form)


def test_password_not_matches(user_form):
    user_form['password_confirmation'] = '123'
    with pytest.raises(PasswordsNotMatchError):
        validate_form(user_form)


def test_user_exists_error(user_form):
    existed_user = {
        'name': 'Alice42',
        'email': 'john42@mail.com'
    }
    users.append(existed_user)
    with pytest.raises(UserExistsError):
        validate_form(user_form)
