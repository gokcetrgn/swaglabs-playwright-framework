def test_verify_overview(overview):
    overview.verify_overview_page()

def test_finish_payment(overview):
    overview.click_finish()
    overview.verify_payment()