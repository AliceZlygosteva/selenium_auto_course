from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from constants import REGISTER_URL, SUCCESS_REGISTER_URL
from locators import USER_NAME_FIELD, PASSWORD_FIELD, CHECKBOX_AGREEMENT, REGISTER_BUTTON
from data import USER_NAME_VALUE, PASSWORD_VALUE

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


def test_register_positive():
    browser.get(REGISTER_URL)

    browser.find_element(*USER_NAME_FIELD).send_keys(USER_NAME_VALUE)
    browser.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_VALUE)

    checkbox = browser.find_element(*CHECKBOX_AGREEMENT)
    checkbox.click()

    assert checkbox.is_selected(), 'checkbox was not executed'

    browser.find_element(*REGISTER_BUTTON).click()

    assert browser.current_url == SUCCESS_REGISTER_URL, 'url не соответствует ожидаемому'


def test_register_negative():
    browser.get(REGISTER_URL)

    browser.find_element(*USER_NAME_FIELD).send_keys(USER_NAME_VALUE)
    browser.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_VALUE)

    browser.find_element(*REGISTER_BUTTON).click()

    assert browser.current_url == REGISTER_URL, 'url не соответствует ожидаемому'
