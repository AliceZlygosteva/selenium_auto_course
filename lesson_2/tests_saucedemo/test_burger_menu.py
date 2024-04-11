from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import AUTH_URL, ABOUT_URL
from locators import BURGER_MENU, LOGOUT, ABOUT, RESET_APP_STATE


def test_logout(browser, auth):  # Выход из системы
    # раскрываем бургер-меню
    browser.find_element(*BURGER_MENU).click()

    # ждём открытия бургер-меню для нажатия ссылки 'Logout'
    wait = WebDriverWait(browser, 5)
    logout_link = wait.until(EC.visibility_of_element_located(LOGOUT))

    # нажимаем 'Logout'
    logout_link.click()

    # проверяем, что произошёл переход на страницу авторизации
    assert browser.current_url == AUTH_URL, 'url не соответствует ожидаемому'


def test_about(browser, auth):  # Проверка работоспособности кнопки "About" в меню
    # раскрываем бургер-меню
    browser.find_element(*BURGER_MENU).click()

    wait = WebDriverWait(browser, 5)
    about_link = wait.until(EC.visibility_of_element_located(ABOUT))

    # нажимаем 'About'
    about_link.click()

    assert browser.current_url == ABOUT_URL, 'url не соответствует ожидаемому'


def test_reset_app_state(browser, auth):  # Проверка работоспособности кнопки "Reset App State"
    # раскрываем бургер-меню
    browser.find_element(*BURGER_MENU).click()

    # ждём открытия бургер-меню для нажатия ссылки 'Reset App State'
    wait = WebDriverWait(browser, 5)
    reset_link = wait.until(EC.visibility_of_element_located(RESET_APP_STATE))

    # нажимаем 'Reset App State'
    reset_link.click()
