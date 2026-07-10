from common.login_loader import DataLoader

data = DataLoader.load("data/SwagLabs/checkout.yml")

def test_checkout(checkout_page):
    checkout_page.fill_checkout_infos(
        "Gokce",
        "TR",
        "34000"
    )
    checkout_page.verify_payment_verify_page()

def test_checkout_req_f_name(checkout_page):
    checkout_page.fill_checkout_infos(
        "",
        "TR",
        "34000"
    )
    checkout_page.verify_error_message(data["messages"]["firstNameReq"])

def test_checkout_req_l_name(checkout_page):
    checkout_page.fill_checkout_infos(
        "sdfs",
        "",
        "34000"
    )
    checkout_page.verify_error_message(data["messages"]["lastNameReq"])

def test_checkout_req_postal_code(checkout_page):
    checkout_page.fill_checkout_infos(
        "dsfsdf",
        "TR",
        ""
    )
    checkout_page.verify_error_message(data["messages"]["postalCodeReq"])