from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import locators


# Переход к разделу "Булки"
def test_go_buns(driver):
    # так как по-умолчанию страница уже на вкладке "Булки", то нам нужно сначала
    # переместиться на другую вкладку конструктора, чтобы "Булки" стало нажимательным
    driver.find_element(*locators.MN_SAUCES).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.HL_SAUCES))

    driver.find_element(*locators.MN_BUNS).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.HL_BUNS))
    assert driver.find_element(*locators.HL_BUNS).text == 'Булки'

# Переход к разделу "Соусы"
def test_go_sauces(driver):
    driver.find_element(*locators.MN_SAUCES).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.HL_SAUCES))
    assert driver.find_element(*locators.HL_SAUCES).text == 'Соусы'

# Переход к разделу "Начинки"
def test_go_fillings(driver):
    driver.find_element(*locators.MN_FILLINGS).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.MN_FILLINGS))
    assert driver.find_element(*locators.HL_FILLINGS).text == 'Начинки'
