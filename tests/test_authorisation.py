from . import constants, base


class TestAuthorization(base.StellarBurgersTestcase):

    # вход по кнопке «Войти в аккаунт» на главной
    def test_authorisation_on_the_homepage(self, driver):
        driver.find_element(*self.home_page.AUTH_BUTTON).click()
        self.login(driver)
        assert self.wait_for(driver, *self.home_page.ORDER_BUTTON)

    # вход через кнопку «Личный кабинет»
    def test_login_via_personal_account(self, driver):
        driver.find_element(*self.home_page.LK_PAGE).click()
        self.login(driver)
        self.wait_for_url(driver, constants.URL_INDEX)
        assert self.wait_for(driver, *self.home_page.ORDER_BUTTON)

    # вход через кнопку в форме регистрации
    def test_auth_by_registr_button(self, driver):
        driver.get(constants.URL_REGISTER)
        self.wait_for(driver, *self.register_page.REG_HEADLINE)
        driver.find_element(*self.register_page.LINK_TO_ENTER).click()
        self.wait_for(driver, *self.login_page.HL_LOGIN)
        self.login(driver)
        assert self.wait_for(driver, *self.home_page.ORDER_BUTTON)

    # вход через кнопку в форме восстановления пароля
    def test_login_button_password_recovery(self, driver):
        driver.get(constants.URL_FORGOT_PASSWORD)
        self.wait_for(driver, *self.recovery_page.HL_PS_RECOVERY)
        driver.find_element(*self.recovery_page.LINK_TO_ENTER).click()
        self.wait_for_url(driver, constants.URL_LOGIN)
        self.login(driver)
        self.wait_for_url(driver, constants.URL_INDEX)
        assert self.wait_for(driver, *self.home_page.ORDER_BUTTON)
