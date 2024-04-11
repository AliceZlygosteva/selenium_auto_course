from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from constants import AUTH_URL, CATALOG_URL
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import LOGIN_VALUE, PASSWORD_VALUE, LOGIN_WRONG_VALUE, PASSWORD_WRONG_VALUE

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


def test_auth_positive():
    browser.get(AUTH_URL)

    # вводим валидный логин в поле 'Username'
    browser.find_element(*USERNAME_FIELD).send_keys(LOGIN_VALUE)

    # вводим валидный пароль в поле 'Password'
    browser.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_VALUE)

    # кликаем на кнопку 'Login'
    browser.find_element(*LOGIN_BUTTON).click()

    assert browser.current_url == CATALOG_URL, 'url не соответствует ожидаемому'


def test_auth_negative():
    browser.get(AUTH_URL)

    # вводим невалидный логин в поле 'Username'
    browser.find_element(*USERNAME_FIELD).send_keys(LOGIN_WRONG_VALUE)

    # вводим невалидный пароль в поле 'Password'
    browser.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_WRONG_VALUE)

    # кликаем на кнопку 'Login'
    browser.find_element(*LOGIN_BUTTON).click()
    assert browser.current_url == AUTH_URL, 'url не соответствует ожидаемому'
