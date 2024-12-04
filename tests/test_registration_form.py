from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import constants, locators
from .routines import random_string


# Успешная регистрация
def test_registration(driver):
    user_name = f"Name{random_string(8)}"
    user_email = f"{random_string(32)}@ya.ru"
    user_password = f"{random_string(6)}"

    driver.find_element(*locators.AUTH_BUTTON).click()
    driver.find_element(*locators.MN_REG_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.REG_HEADLINE))

    driver.find_element(*locators.NAME).send_keys(user_name)
    driver.find_element(*locators.EMAIL).send_keys(user_email)
    driver.find_element(*locators.PASSWORD).send_keys(user_password)
    driver.find_element(*locators.REG_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.url_to_be(constants.URL_LOGIN))
    assert driver.current_url == constants.URL_LOGIN

# некорректный пароль
def test_registration_invalid_password(driver):
    user_name = f"Name{random_string(8)}"
    user_email = f"{random_string(32)}@ya.ru"
    user_password = f"{random_string(4)}"

    driver.get(constants.URL_REGISTER)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.REG_HEADLINE))
    driver.find_element(*locators.NAME).send_keys(user_name)
    driver.find_element(*locators.EMAIL).send_keys(user_email)
    driver.find_element(*locators.PASSWORD).send_keys(user_password)
    driver.find_element(*locators.REG_BUTTON).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.INV_PASSWORD))
    error_mes = driver.find_element(*locators.INV_PASSWORD)
    assert error_mes.text == 'Некорректный пароль'
