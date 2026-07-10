import allure

from projects.Swaglabs.pages.login_page import LoginPage
from playwright.sync_api import expect


class LoginSteps:

    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)

    @allure.step("Sayfa başlığı doğrulanır")

    def verify_title(self):
        expect(self.page).to_have_title("Swag Labs")

    @allure.step("Kullanıcı adı ve şifre ile giriş yapılır")
    def login(self, username, password):
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()


    # page verification
    @allure.step("Anasayfaya geçiş doğrulanır")
    def verify_home_page(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )


    # error message
    @allure.step("Error mesajları doğrulanır")
    def verify_error_message(self, expected_message):
        expect(
            self.login_page.error_message
        ).to_have_text(expected_message)

    @allure.step("Error mesajları görünürlüğü kontrol edilir")
    def verify_error_message_visible(self):
        expect(
            self.login_page.error_message
        ).to_be_visible()

    @allure.step("Error mesajlarını X ile kapatma kontrolü yapılır")
    def close_error_message(self):
        self.login_page.close_error()

    @allure.step("Kapattıktan sonra görünür olmadığı kontrol edilir")
    def verify_error_message_not_visible(self):
        expect(
            self.login_page.error_message
        ).not_to_be_visible()


    # username

    @allure.step("Kullanıcı adı görünürlüğü kontrolü")
    def verify_username_input_is_visible(self):
        expect(
            self.login_page.username_input
        ).to_be_visible()

    @allure.step("Kullanıcı adı textfieldına erişim kontrolü")
    def verify_username_input_is_enabled(self):
        expect(
            self.login_page.username_input
        ).to_be_enabled()
    @allure.step("Kullanıcı adı boş mu geliyor kontrolü")
    def verify_username_empty(self):
        expect(self.login_page.username_input).to_be_empty()

    @allure.step("Kullanıcı adı placeholder kontrolü")
    def verify_username_placeholder(self):
        expect(
            self.login_page.username_input
        ).to_have_attribute(
            "placeholder",
            "Username"
        )


    # password
    @allure.step("Şifre textfieldı görünür mü kontrolü")
    def verify_password_input_is_visible(self):
        expect(
            self.login_page.password_input
        ).to_be_visible()

    @allure.step("Şifre txtfieldı erişilebilir mi?")
    def verify_password_input_is_enabled(self):
        expect(
            self.login_page.password_input
        ).to_be_enabled()
    @allure.step("Şifre boş mu geliyor")
    def verify_password_empty(self):
        expect(self.login_page.password_input).to_be_empty()

    @allure.step("Şifre typeı kontrolü")
    def verify_password_type(self):
        expect(
            self.login_page.password_input
        ).to_have_attribute(
            "type",
            "password"
        )

    @allure.step("Şifre placeholder ı kontrolü")
    def verify_password_placeholder(self):
        expect(
            self.login_page.password_input
        ).to_have_attribute(
            "placeholder",
            "Password"
        )


    # login button
    @allure.step("Login butonu tıklanabilir mi?")
    def verify_login_button_is_clickable(self):
        expect(
            self.login_page.login_button
        ).to_be_enabled()

    @allure.step("Buton texti kontrolü")
    def verify_login_button_text(self):
        expect(
            self.login_page.login_button
        ).to_have_value(
            "Login"
        )


    # Kkeyboard
    @allure.step("Enter tuşuna basma işlemi")
    def login_with_enter(self):
        self.login_page.press_enter()