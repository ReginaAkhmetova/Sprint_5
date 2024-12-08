from . import base


class TestConstructor(base.StellarBurgersTestcase):

    # Переход к разделу "Булки"
    def test_go_buns(self, driver):
        # так как по-умолчанию страница уже на вкладке "Булки", то нам нужно сначала
        # переместиться на другую вкладку конструктора, чтобы "Булки" стало нажимательным
        driver.find_element(*self.home_page.MN_SAUCES).click()
        self.wait_for_visible(driver, *self.home_page.HL_SAUCES)

        driver.find_element(*self.home_page.MN_BUNS).click()
        self.wait_for_visible(driver, *self.home_page.HL_BUNS)
        assert driver.find_element(*self.home_page.HL_BUNS).text == 'Булки'

    # Переход к разделу "Соусы"
    def test_go_sauces(self, driver):
        driver.find_element(*self.home_page.MN_SAUCES).click()
        self.wait_for_visible(driver, *self.home_page.HL_SAUCES)
        assert driver.find_element(*self.home_page.HL_SAUCES).text == 'Соусы'

    # Переход к разделу "Начинки"
    def test_go_fillings(self, driver):
        driver.find_element(*self.home_page.MN_FILLINGS).click()
        self.wait_for_visible(driver, *self.home_page.MN_FILLINGS)
        assert driver.find_element(*self.home_page.HL_FILLINGS).text == 'Начинки'
