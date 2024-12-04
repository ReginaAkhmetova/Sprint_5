from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import constants, locators
from .routines import authenticate


# вход по кнопке «Войти в аккаунт» на главной
def test_authorisation_on_the_homepage(driver):
    driver.find_element(*locators.AUTH_BUTTON).click()
    authenticate(driver)
    assert WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.ORDER_BUTTON))


# вход через кнопку «Личный кабинет»
def test_login_via_personal_account(driver):
    driver.find_element(*locators.LK_PAGE).click()
    authenticate(driver)
    assert WebDriverWait(driver, 3).until(EC.url_to_be(constants.URL_INDEX))


# вход через кнопку в форме регистрации
def test_auth_by_registr_button(driver):
    driver.get(constants.URL_REGISTER)
    driver.find_element(*locators.LINK_TO_ENTER).click()
    authenticate(driver)
    assert WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.ORDER_BUTTON))


# вход через кнопку в форме восстановления пароля
def test_login_button_password_recovery(driver):
    driver.get(constants.URL_FORGOT_PASSWORD)
    driver.find_element(*locators.LINK_TO_ENTER).click()
    assert driver.current_url == constants.URL_LOGIN
