import pytest
from selenium import webdriver

from . import constants


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1500,1000')
    driver = webdriver.Chrome(chrome_options)
    driver.get(constants.URL_INDEX)
    yield driver
    driver.quit()

