from selenium.webdriver.common.by import By


MN_REG_BUTTON = (By.CSS_SELECTOR, 'a[href="/register"]')  # кнопка Зарегистрироваться в главном меню
REG_HEADLINE = (By.XPATH, ".//h2[text()='Регистрация']")  # Заголовок Регистрация
REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # кнопка Зарегистр-ся в окне регистрации

NAME = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[1]")  # Поле Имя
EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input[1]")  # Поле email
PASSWORD = (By.NAME, "Пароль")  # Поле Пароль

INV_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")  # ошибка с текстом некорректный пароль
RECOVER_PASSWORD = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')  # восстановить пароль

LINK_TO_ENTER = (By.CSS_SELECTOR, 'a[href="/login"]')  # ссылка Войти

LK_PAGE = (By.XPATH, ".//p[text()='Личный Кабинет']")  #  личный кабинет на главной странице
MN_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, 'a[href="/account"]') # личный кабинет
ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка Оформить заказ

AUTH_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка Войти в аккаунт
HL_LOGIN = (By.XPATH, ".//h2[text()='Вход']")  # заголовок Вход
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # кнопка Войти
HL_PS_RECOVERY = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # восстановление пароля
LOG_OUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # кнопка Выход

MN_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']") # Конструктор
LOGO = (By.TAG_NAME, "svg")  # Логотип  Stellar Burgers

MN_BUNS = (By.XPATH, ".//span[text()='Булки']/parent::*")  # раздел Булки
HL_BUNS = (By.XPATH, ".//h2[text()='Булки']")  # заголовок ингридиентов Булки
MN_SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::*")  # раздел Соусы
HL_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")  # заголовок Соусы
MN_FILLINGS = (By.XPATH, ".//span[text()='Начинки']/parent::*")  # раздел Начинки
HL_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")  # заголовок Начинки
