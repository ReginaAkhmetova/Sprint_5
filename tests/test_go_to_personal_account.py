from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import locators, constants
from .routines import authenticate


# переход в «Личный кабинет»
def test_go_to_personal_account(driver):
    driver.find_element(*locators.MN_PERSONAL_ACCOUNT).click()
    authenticate(driver)
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.MN_PERSONAL_ACCOUNT))
    driver.find_element(*locators.MN_PERSONAL_ACCOUNT).click()
    assert WebDriverWait(driver, 3).until(EC.url_to_be(constants.URL_PROFILE))
