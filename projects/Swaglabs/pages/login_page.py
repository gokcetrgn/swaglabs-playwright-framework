from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page : Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
        self.error_close_button = page.locator(".error-button")

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def press_enter(self):
        self.password_input.press("Enter")

    def close_error(self):
        self.error_close_button.click()

    def get_error_message(self):
        return self.error_message.text_content()

    def get_username_placeholder(self):
        return self.username_input.get_attribute("placeholder")

    def get_password_placeholder(self):
        return self.password_input.get_attribute("placeholder")

    def get_password_type(self):
        return self.password_input.get_attribute("type")

    def get_login_button_text(self):
        return self.login_button.input_value()

