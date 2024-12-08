from . import base, constants


class TestGotoPersonalAccount(base.StellarBurgersTestcase):

    # переход в «Личный кабинет»
    def test_go_to_personal_account(self, driver):
        driver.find_element(*self.home_page.MN_PERSONAL_ACCOUNT).click()
        self.login(driver)
        self.wait_for_clickable(driver, *self.home_page.MN_PERSONAL_ACCOUNT)
        driver.find_element(*self.home_page.MN_PERSONAL_ACCOUNT).click()
        assert self.wait_for_url(driver, constants.URL_PROFILE)
