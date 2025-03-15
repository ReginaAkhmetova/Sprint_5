from . import constants, base


class TestLkToConstructor(base.StellarBurgersTestcase):
    # Переход из личного кабинета по клику на «Конструктор
    def test_from_lk_to_the_constructor(self, driver):
        driver.find_element(*self.home_page.LK_PAGE).click()
        self.login(driver)

        self.wait_for_clickable(driver, *self.home_page.MN_PERSONAL_ACCOUNT)

        driver.find_element(*self.home_page.MN_PERSONAL_ACCOUNT).click()
        self.wait_for(driver, *self.account_page.MN_CONSTRUCTOR)
        driver.find_element(*self.account_page.MN_CONSTRUCTOR).click()

        assert self.wait_for_url(driver, constants.URL_INDEX)


    # Переход из личного кабинета по клику на логотип Stellar Burgers.
    def test_logo_stellar_burgers(self, driver):
        driver.find_element(*self.home_page.LK_PAGE).click()
        self.login(driver)

        self.wait_for_clickable(driver, *self.home_page.MN_PERSONAL_ACCOUNT)

        driver.find_element(*self.home_page.MN_PERSONAL_ACCOUNT).click()
        driver.find_element(*self.LOGO).click()

        assert self.wait_for_url(driver, constants.URL_INDEX)
