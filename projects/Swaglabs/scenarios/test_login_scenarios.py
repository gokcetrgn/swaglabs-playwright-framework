import pytest

from projects.Swaglabs.cases.login_steps import LoginSteps

from common.login_loader import DataLoader

data = DataLoader.load("data/SwagLabs/login.yml")

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

def test_valid_login(app):
    steps = LoginSteps(app)
    steps.login(data["invalidUser"]["username"],
                data["validUser"]["password"])

    steps.verify_home_page()

def test_problem_user_login(app):
    steps = LoginSteps(app)
    steps.login(data["problemUser"]["username"],
                data["problemUser"]["password"])

    steps.verify_home_page()

def test_performance_user_login(app):
    steps = LoginSteps(app)
    steps.login(data["perfUser"]["username"],
                data["perfUser"]["password"])

    steps.verify_home_page()

def test_invalid_login(app):
    steps = LoginSteps(app)
    steps.login(data["invalidUser"]["username"],
                data["invalidUser"]["password"])

    steps.verify_error_message(data["messages"]["invalid"])


def test_locked_login(app):
    steps = LoginSteps(app)
    steps.login(data["lockedUser"]["username"],
                data["lockedUser"]["password"])

    steps.verify_error_message(data["messages"]["locked"])

def test_login_with_enter(app):

    steps = LoginSteps(app)

    steps.login_page.enter_username(
        data["validUser"]["username"]
    )

    steps.login_page.enter_password(
        data["validUser"]["password"]
    )

    steps.login_page.press_enter()

    steps.verify_home_page()
def test_true_password_username_req(app):
    steps = LoginSteps(app)
    steps.login("",
                data["validUser"]["password"])

    steps.verify_error_message(data["messages"]["usernameReq"])

def test_true_username_password_req(app):
    steps = LoginSteps(app)
    steps.login(data["validUser"]["username"],
                "")

    steps.verify_error_message(data["messages"]["passwordReq"])

@pytest.mark.smoke
def test_false_password_username_req(app):
    steps = LoginSteps(app)
    steps.login("",
                data["invalidUser"]["password"])

    steps.verify_error_message(data["messages"]["usernameReq"])

@pytest.mark.negative
def test_false_username_password_req(app):
    steps = LoginSteps(app)
    steps.login(data["invalidUser"]["username"],
                "")

    steps.verify_error_message(data["messages"]["passwordReq"])

@pytest.mark.negative

def test_both_username_password_req(app):
    steps = LoginSteps(app)
    steps.login("",
                "")

    steps.verify_error_message(data["messages"]["usernameReq"])

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