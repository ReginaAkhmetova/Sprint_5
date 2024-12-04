import random
import string

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import constants, locators


def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def authenticate(driver):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.HL_LOGIN))
    driver.find_element(*locators.EMAIL).send_keys(constants.EMAIL)
    driver.find_element(*locators.PASSWORD).send_keys(constants.PASSWORD)
    driver.find_element(*locators.LOGIN_BUTTON).click()
