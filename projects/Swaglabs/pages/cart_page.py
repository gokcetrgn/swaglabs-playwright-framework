from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.remove_buttons = page.locator(".cart_button")
        self.continue_btn = page.locator("#continue-shopping")
        self.checkout = page.locator("#checkout")




