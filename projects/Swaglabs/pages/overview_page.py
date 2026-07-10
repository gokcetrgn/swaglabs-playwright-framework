from playwright.sync_api import Page


class OverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.cancelBtn = page.locator("#cancel")
        self.finishBtn = page.locator("#finish")

    def click_finish(self):
        self.finishBtn.click()

    def click_cancel(self):
        self.cancelBtn.click()
