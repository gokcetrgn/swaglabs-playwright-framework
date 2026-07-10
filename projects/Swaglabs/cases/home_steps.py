from playwright.sync_api import expect

from projects.Swaglabs.pages.home_page import HomePage

class HomeSteps:
    def __init__(self,page):
        self.page = page
        self.home_page = HomePage(page)

    def verify_home_page(self):
        expect(self.page.locator(".title")).to_have_text("Products")
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )
    def verify_login_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/")

    def click_product_photo(self, product_id):
        self.page.locator(f"#item_{product_id}_img_link").click()

    def click_product_title(self,product_id):
        self.page.locator(f"#item_{product_id}_title_link").click()

    def verify_product_nav(self,product_id):
        expect(self.page).to_have_url(
            f"https://www.saucedemo.com/inventory-item.html?id={product_id}"
        )
    def click_add_to_cart_button(self, product_id: int):
        self.page.locator(
            f'[data-test="item-{product_id}-img-link"]'
        ).locator("xpath=ancestor::div[@class='inventory_item']").locator("button").click()

    def click_remove_button(self,product_id: int):
        self.page.locator(
            f'[data-test="item-{product_id}-img-link"]'
        ).locator("xpath=ancestor::div[@class='inventory_item']").locator("button").click()


    def verify_cart_is_empty(self):
        expect(self.page.locator(".shopping_cart_badge")).to_have_count(0)

    def verify_cart_badge(self, expected_count):
        expect(self.page.locator(".shopping_cart_badge")).to_have_text(str(expected_count))

    def click_filter(self):
        self.home_page.filter.click()

    def click_option_filter(self,option):
        self.home_page.filter.select_option(option)

    def go_to_about_from_menu(self):
        self.home_page.click_menu_icon()
        self.home_page.about.click()

    def verify_about_link(self):
        expect(self.page).to_have_url("https://saucelabs.com/")
    def go_to_cart_page(self):
        self.home_page.click_cart_icon()

    def verify_cart_page(self):
        expect(self.page.locator(".title")).to_have_text("Your Cart")
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/cart.html")

    def verify_sort_by_name(self, ascending=True):
        names = self.home_page.product_names.all_text_contents()

        expected = sorted(names)
        if not ascending:
            expected = sorted(names, reverse=True)

        assert names == expected

    def verify_sort_by_price(self, ascending=True):
        prices = [
            float(price.replace("$", ""))
            for price in self.home_page.product_prices.all_text_contents()
        ]

        expected = sorted(prices)
        if not ascending:
            expected = sorted(prices, reverse=True)

        assert prices == expected


    def logout(self):
        self.home_page.click_menu_icon()
        self.home_page.logout.click()