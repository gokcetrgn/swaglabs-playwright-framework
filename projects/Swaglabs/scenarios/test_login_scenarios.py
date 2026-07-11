import pytest
from projects.Swaglabs.cases.login_steps import LoginSteps

from common.login_loader import DataLoader

config = DataLoader.load("data/SwagLabs/config.yml")
users = DataLoader.load_json("data/SwagLabs/login_users.json")

EXPECTED_MESSAGES = {
    "locked": config["messages"]["locked"],
    "invalid": config["messages"]["invalid"],
    "username_required": config["messages"]["usernameReq"],
    "password_required": config["messages"]["passwordReq"],
}

@pytest.mark.ui
def test_page_title(app):

    steps = LoginSteps(app)

    steps.verify_title()

@pytest.mark.ui
def test_username_txf(app):

    steps = LoginSteps(app)

    steps.verify_username_input_is_visible()
    steps.verify_username_input_is_enabled()

def test_password_txf(app):

    steps = LoginSteps(app)

    steps.verify_password_input_is_visible()
    steps.verify_password_input_is_enabled()


@pytest.mark.smoke
def test_login_button(app):

    steps = LoginSteps(app)

    steps.verify_login_button_is_clickable()

@pytest.mark.parametrize("user", users, ids=[u["name"] for u in users])
def test_login(app, user):
    steps = LoginSteps(app)
    steps.login(user["username"], user["password"])


    if user["result"] == "success":
        steps.verify_home_page()
    else:
        steps.verify_error_message(EXPECTED_MESSAGES[user["result"]])

#UI tests

def test_login_button_text(app):

    steps = LoginSteps(app)

    steps.verify_login_button_text()

def test_username_placeholder(app):

    steps = LoginSteps(app)

    steps.verify_username_placeholder()

def test_password_placeholder(app):

    steps = LoginSteps(app)

    steps.verify_password_placeholder()

def test_password_field_type(app):

    steps = LoginSteps(app)

    steps.verify_password_type()

def test_username_empty(app):

    steps = LoginSteps(app)

    steps.verify_username_empty()

def test_password_empty(app):

    steps = LoginSteps(app)

    steps.verify_password_empty()

# close error message
@pytest.mark.smoke
def test_close_error_message(app):

    steps = LoginSteps(app)

    steps.login("", "")

    steps.verify_error_message_visible()

    steps.close_error_message()

    steps.verify_error_message_not_visible()