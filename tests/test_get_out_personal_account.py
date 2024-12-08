from . import constants, base


class TestGetOutPersonalAccount(base.StellarBurgersTestcase):
    # выход по кнопке «Выйти» в личном кабинете
    def test_get_out_personal_account(self, driver):
        driver.get(constants.URL_LOGIN)
        self.login(driver)

        self.wait_for_clickable(driver, *self.home_page.LK_PAGE)
        driver.find_element(*self.home_page.LK_PAGE).click()
        self.wait_for_url(driver, constants.URL_PROFILE)
        driver.find_element(*self.account_page.LOG_OUT_BUTTON).click()

        assert self.wait_for_url(driver, constants.URL_LOGIN)
