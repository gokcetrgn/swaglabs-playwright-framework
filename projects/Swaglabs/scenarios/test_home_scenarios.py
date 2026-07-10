import pytest
def test_home_page(home):
    home.verify_home_page()

def test_navigate_with_product_photo(home):
    home.click_product_photo()
    home.verify_product_nav()

def test_navigate_with_product_title(home):
    home.click_product_title(4)
    home.verify_product_nav(4)

def test_add_to_cart(home):
    home.click_add_to_cart_button(4)
    home.verify_cart_badge(1)

def test_remove_when_only_one(home):
    home.click_add_to_cart_button(4)
    home.click_remove_button(4)
    home.verify_cart_is_empty()

def test_remove(home):
    home.click_add_to_cart_button(4)
    home.click_add_to_cart_button(2)
    home.click_remove_button(4)
    home.verify_cart_badge(1)

@pytest.mark.sort
@pytest.mark.parametrize(
    "sort_type, ascending, sort_by",
    [
        ("az", True, "name"),
        ("za", False, "name"),
        ("lohi", True, "price"),
        ("hilo", False, "price"),
    ]
)
def test_sort(home, sort_type, ascending, sort_by):
    home.click_option_filter(sort_type)

    if sort_by == "name":
        home.verify_sort_by_name(ascending)
    else:
        home.verify_sort_by_price(ascending)


def test_navigate_to_about(home):
    home.go_to_about_from_menu()
    home.verify_about_link()

def test_navigate_to_cart_page(home):
    home.go_to_cart_page()
    home.verify_cart_page()


def test_logout(home):
    home.logout()
    home.verify_login_page()