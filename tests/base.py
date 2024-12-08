import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import constants


class HomePage:
    AUTH_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка Войти в аккаунт
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка Оформить заказ
    LK_PAGE = (By.XPATH, ".//p[text()='Личный Кабинет']")  # личный кабинет на главной странице
    MN_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, 'a[href="/account"]')  # личный кабинет

    MN_BUNS = (By.XPATH, ".//span[text()='Булки']/parent::*")  # раздел Булки
    HL_BUNS = (By.XPATH, ".//h2[text()='Булки']")  # заголовок ингридиентов Булки
    MN_SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::*")  # раздел Соусы
    HL_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")  # заголовок Соусы
    MN_FILLINGS = (By.XPATH, ".//span[text()='Начинки']/parent::*")  # раздел Начинки
    HL_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")  # заголовок Начинки


class LoginPage:
    HL_LOGIN = (By.XPATH, ".//h2[text()='Вход']")  # заголовок Вход
    EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input[1]")  # Поле email
    PASSWORD = (By.NAME, "Пароль")  # Поле Пароль
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # кнопка Войти
    MN_REG_BUTTON = (By.CSS_SELECTOR, 'a[href="/register"]')  # кнопка Зарегистрироваться в главном меню


class RegisterPage:
    REG_HEADLINE = (By.XPATH, ".//h2[text()='Регистрация']")  # Заголовок Регистрация
    NAME = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[1]")  # Поле Имя
    EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input[1]")  # Поле email
    PASSWORD = (By.NAME, "Пароль")  # Поле Пароль
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка Зарегистр-ся в окне регистрации
    LINK_TO_ENTER = (By.CSS_SELECTOR, 'a[href="/login"]')  # ссылка Войти
    INV_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")  # ошибка с текстом некорректный пароль


class RecoveryPage:
    HL_PS_RECOVERY = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # восстановление пароля
    LINK_TO_ENTER = (By.CSS_SELECTOR, 'a[href="/login"]')  # ссылка Войти


class PersonalAccountPage:
    MN_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")  # Конструктор
    LOG_OUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # кнопка Выход


class StellarBurgersTestcase:
    home_page = HomePage()
    login_page = LoginPage()
    register_page = RegisterPage()
    recovery_page = RecoveryPage()
    account_page = PersonalAccountPage()

    LOGO = (By.TAG_NAME, "svg")  # Логотип  Stellar Burgers

    @classmethod
    def login(cls, driver, email=constants.EMAIL, password=constants.PASSWORD):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(cls.login_page.HL_LOGIN))
        driver.find_element(*cls.login_page.EMAIL).send_keys(email)
        driver.find_element(*cls.login_page.PASSWORD).send_keys(password)
        driver.find_element(*cls.login_page.LOGIN_BUTTON).click()

    @staticmethod
    def random_string(length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    @classmethod
    def get_random_reqs(cls, passwrd_length=6):
        return (
            f"Name{cls.random_string(8)}",
            f"{cls.random_string(32)}@ya.ru",
            f"{cls.random_string(passwrd_length)}"
        )

    @classmethod
    def wait_for(cls, driver, by, loc):
        return WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, loc)))

    @classmethod
    def wait_for_visible(cls, driver, by, loc):
        return WebDriverWait(driver, 3).until(EC.visibility_of_element_located((by, loc)))

    @classmethod
    def wait_for_clickable(cls, driver, by, loc):
        return WebDriverWait(driver, 3).until(EC.element_to_be_clickable((by, loc)))

    @classmethod
    def wait_for_url(cls, driver, url):
        return WebDriverWait(driver, 3).until(EC.url_to_be(url))
