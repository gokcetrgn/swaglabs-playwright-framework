import allure
import pytest
from common.config_loader import ConfigLoader
from projects.Swaglabs.cases.cart_page_steps import CartSteps
from projects.Swaglabs.cases.home_steps import HomeSteps
from projects.Swaglabs.cases.login_steps import LoginSteps

from common.login_loader import DataLoader
from projects.Swaglabs.cases.checkout_steps import CheckoutSteps
from projects.Swaglabs.cases.overview_steps import OverviewSteps

data = DataLoader.load("data/SwagLabs/login.yml")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def app(browser, playwright, request):

    config = ConfigLoader.load()

    context_args = {"record_video_dir": "results/videos"}

    context = browser.new_context(**context_args)

    page = context.new_page()

    page.goto(config["application"]["base_url"])

    yield page

    context.close()

    if request.node.rep_call.failed:
        allure.attach.file(
            page.video.path(),
            name="Test Videosu",
            attachment_type=allure.attachment_type.WEBM
        )


@pytest.fixture
def logged_in_app(app):
    login = LoginSteps(app)
    login.login(
        data["validUser"]["username"],
        data["validUser"]["password"]
    )
    return app
@pytest.fixture
def home(logged_in_app):
    return HomeSteps(logged_in_app)

@pytest.fixture
def cart(logged_in_app):
    return CartSteps(logged_in_app)

@pytest.fixture
def checkout(logged_in_app):
    return CheckoutSteps(logged_in_app)

@pytest.fixture
def overview(logged_in_app):
    return OverviewSteps(logged_in_app)

@pytest.fixture
def cart_with_products(home):
    home.click_add_to_cart_button(4)
    home.click_add_to_cart_button(2)
    home.go_to_cart_page()
    return home

@pytest.fixture
def checkout_page(home, cart, logged_in_app):
    home.click_add_to_cart_button(4)
    home.go_to_cart_page()
    cart.click_checkout_btn()
    return CheckoutSteps(logged_in_app)

@pytest.fixture
def overview(home, cart, checkout,logged_in_app):
    home.click_add_to_cart_button(4)
    home.go_to_cart_page()
    cart.click_checkout_btn()
    checkout.fill_checkout_infos("Gokce","sdkfdskd","555555")
    return OverviewSteps(logged_in_app)