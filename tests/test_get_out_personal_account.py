from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import constants, locators
from .routines import authenticate


# выход по кнопке «Выйти» в личном кабинете
def test_get_out_personal_account(driver):
    driver.get(constants.URL_LOGIN)
    authenticate(driver)

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.LK_PAGE))
    driver.find_element(*locators.LK_PAGE).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(constants.URL_PROFILE))
    driver.find_element(*locators.LOG_OUT_BUTTON).click()

    assert WebDriverWait(driver, 3).until(EC.url_to_be(constants.URL_LOGIN))
