import re

from repository import users
from errors import InvalidEmailError, PasswordsNotMatchError, UserExistsError


def validate_email(email):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if email_regex.match(email):
        return True
    return False


# BEGIN (write your solution here)
def validate_name(user_name):
    exist_names = (user['email'] for user in users)
    for exist_name in exist_names:
        if exist_name == user_name:
            return False
    return True

def validate_form(user_form):
    email = user_form['email']
    password = user_form['password']
    confirmed_pass = user_form['password_confirmation']

    if not validate_email(email):
        raise InvalidEmailError
    if password != confirmed_pass:
        raise PasswordsNotMatchError
    for user in users:
        if user['email'] == email:
            raise UserExistsError
    return True
# END
