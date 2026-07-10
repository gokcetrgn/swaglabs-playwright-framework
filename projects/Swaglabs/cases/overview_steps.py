from projects.Swaglabs.pages.overview_page import OverviewPage
from playwright.sync_api import expect


class OverviewSteps:

    def __init__(self, page):
        self.page = page
        self.overview_page = OverviewPage(page)

    def verify_overview_page(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Overview")
        expect(self.page).to_have_url(
           "https://www.saucedemo.com/checkout-step-two.html"
        )

    def click_finish(self):
        self.overview_page.click_finish()

    def verify_payment(self):
        expect(self.page.locator(".title")).to_have_text("Checkout: Complete!")
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-complete.html"
        )