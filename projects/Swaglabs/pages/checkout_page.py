from playwright.sync_api import Page

class Checkout:
    def __init__(self, page: Page):
        self.page = page
        self.fName = page.locator("#first-name")
        self.lName = page.locator("#last-name")
        self.postalCode = page.locator("#postal-code")
        self.cancel = page.locator("#cancel")
        self.continueBtn = page.locator("#continue")
        self.error_message = page.locator("[data-test='error']")
        self.error_close_button = page.locator(".error-button")


    def enter_firstname(self, first_name):
        self.fName.fill(first_name)

    def enter_lastname(self, lastname):
        self.lName.fill(lastname)

    def enter_postal_code(self, postalcode):
        self.postalCode.fill(postalcode)

    def click_cancel(self):
        self.cancel.click()

    def click_continue(self):
        self.continueBtn.click()

    def close_error(self):
        self.error_close_button.click()

    def get_error_message(self):
        return self.error_message.text_content()
