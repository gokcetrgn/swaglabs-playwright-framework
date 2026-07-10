from projects.Swaglabs.pages.checkout_page import Checkout
from playwright.sync_api import expect


class CheckoutSteps:

    def __init__(self, page):
        self.page = page
        self.checkout_page = Checkout(page)

    def verify_checkout_page(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Your Information")
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-step-one.html")


    def verify_payment_verify_page(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Overview")
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    def fill_checkout_infos(self, fname, lname, postal_code):
        self.checkout_page.enter_firstname(fname)
        self.checkout_page.enter_lastname(lname)
        self.checkout_page.enter_postal_code(postal_code)
        self.checkout_page.click_continue()
    def verify_error_message(self, expected_message):
        expect(
            self.checkout_page.error_message
        ).to_have_text(expected_message)
