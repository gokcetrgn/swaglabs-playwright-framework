from playwright.sync_api import expect

from projects.Swaglabs.pages.cart_page import CartPage

class CartSteps:
    def __init__(self,page):
        self.page = page
        self.cart_page = CartPage(page)

    def click_remove_item(self, index):
        self.cart_page.remove_buttons.nth(index).click()

    def verify_item_count(self, expected_count):
        expect(self.cart_page.remove_buttons).to_have_count(expected_count)

    def click_continue_btn(self):
        self.cart_page.continue_btn.click()

    def click_checkout_btn(self):
        self.cart_page.checkout.click()

    def verify_continue_btn(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def verify_checkout(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Your Information")
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

