import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from constants import AUTH_URL, CATALOG_URL
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import LOGIN_VALUE, PASSWORD_VALUE


@pytest.fixture()
def browser():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    print('\nquit browser...')
    browser.quit()


@pytest.fixture()
def auth(browser):
    browser.get(AUTH_URL)
    browser.find_element(*USERNAME_FIELD).send_keys(LOGIN_VALUE)
    browser.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_VALUE)
    browser.find_element(*LOGIN_BUTTON).click()

    assert browser.current_url == CATALOG_URL, 'url не соответствует ожидаемому'
