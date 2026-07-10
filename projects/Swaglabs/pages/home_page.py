from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.filter = page.locator(".product_sort_container")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.all_items = page.locator("#inventory_sidebar_link")
        self.about = page.locator("#about_sidebar_link")
        self.logout = page.locator("#logout_sidebar_link")
        self.reset_app_state = page.locator("#reset_sidebar_link")
        self.cart = page.locator(".shopping_cart_link")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")

    def product_image(self, product_id: int):
        return self.page.locator(f"#item_{product_id}_img_link")

    def product_title(self, product_id: int):
        return self.page.locator(f"#item_{product_id}_title_link")

    def add_to_cart_button(self, product_name: str):
        product_name = product_name.lower().replace(" ", "-")
        return self.page.locator(f"#add-to-cart-{product_name}")

    def click_card_photo(self, product_id: int):
        self.product_image(product_id).click()

    def click_card_title(self, product_id: int):
        self.product_title(product_id).click()

    def click_add_to_cart(self, product_name: str):
        self.add_to_cart_button(product_name).click()



    def click_menu_icon(self):
        self.menu_button.click()

    def click_cart_icon(self):
        self.cart.click()