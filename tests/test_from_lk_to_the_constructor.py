from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import constants, locators
from .routines import authenticate

# Переход из личного кабинета по клику на «Конструктор
def test_from_lk_to_the_constructor(driver):
    driver.find_element(*locators.LK_PAGE).click()
    authenticate(driver)

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.MN_PERSONAL_ACCOUNT))

    driver.find_element(*locators.MN_PERSONAL_ACCOUNT).click()
    driver.find_element(*locators.MN_CONSTRUCTOR).click()

    assert WebDriverWait(driver, 3).until(EC.url_to_be(constants.URL_INDEX))


# Переход из личного кабинета по клику на логотип Stellar Burgers.
def test_logo_stellar_burgers(driver):
    driver.find_element(*locators.LK_PAGE).click()
    authenticate(driver)

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.MN_PERSONAL_ACCOUNT))

    driver.find_element(*locators.MN_PERSONAL_ACCOUNT).click()
    driver.find_element(*locators.LOGO).click()

    assert WebDriverWait(driver, 3).until(EC.url_to_be(constants.URL_INDEX))
