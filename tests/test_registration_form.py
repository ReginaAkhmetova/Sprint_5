from . import constants, base


class TestRegistration(base.StellarBurgersTestcase):

    # Успешная регистрация
    def test_registration(self, driver):
        user_name, user_email, user_password = self.get_random_reqs()

        driver.find_element(*self.home_page.AUTH_BUTTON).click()
        self.wait_for(driver, *self.login_page.HL_LOGIN)
        driver.find_element(*self.login_page.MN_REG_BUTTON).click()

        self.wait_for(driver, *self.register_page.REG_HEADLINE)
        driver.find_element(*self.register_page.NAME).send_keys(user_name)
        driver.find_element(*self.register_page.EMAIL).send_keys(user_email)
        driver.find_element(*self.register_page.PASSWORD).send_keys(user_password)
        driver.find_element(*self.register_page.REG_BUTTON).click()

        self.wait_for_url(driver, constants.URL_LOGIN)
        assert driver.current_url == constants.URL_LOGIN

    # некорректный пароль
    def test_registration_invalid_password(self, driver):
        user_name, user_email, user_password = self.get_random_reqs(4)

        driver.get(constants.URL_REGISTER)
        self.wait_for(driver, *self.register_page.REG_HEADLINE)
        driver.find_element(*self.register_page.NAME).send_keys(user_name)
        driver.find_element(*self.register_page.EMAIL).send_keys(user_email)
        driver.find_element(*self.register_page.PASSWORD).send_keys(user_password)
        driver.find_element(*self.register_page.REG_BUTTON).click()

        self.wait_for(driver, *self.register_page.INV_PASSWORD)
        error_mes = driver.find_element(*self.register_page.INV_PASSWORD)
        assert error_mes.text == 'Некорректный пароль'
