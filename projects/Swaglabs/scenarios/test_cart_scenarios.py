def test_remove_product(cart_with_products, cart):
    cart.click_remove_item(0)
    cart.verify_item_count(1)


def test_go_to_payment(cart_with_products, cart):
    cart.click_checkout_btn()
    cart.verify_checkout()

def test_return_home_w_continue(home,cart):
    home.go_to_cart_page()
    cart.click_continue_btn()
    cart.verify_continue_btn()


