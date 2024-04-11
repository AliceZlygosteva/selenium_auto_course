from locators import (ADD_TO_CART_BUTTON_IN_CATALOG, CART_ICON, CHECKOUT_BUTTON, FIRST_NAME_FIELD, LAST_NAME_FIELD,
                      POSTAL_CODE_FIELD, CHECKOUT_CONTINUE_BUTTON, CHECKOUT_FINISH_BUTTON, BACK_TO_PRODUCTS_BUTTON)
from constants import CART_URL, CATALOG_URL, CHECKOUT_COMPLETE_URL, CHECKOUT_STEP_1_URL, CHECKOUT_STEP_2_URL
from data import FIRST_NAME_VALUE, LAST_NAME_VALUE, POSTAL_CODE_VALUE


def test_checkout(browser, auth):  # Оформление заказа используя корректные данные
    # кликаем на кнопку 'Add to cart'
    browser.find_element(*ADD_TO_CART_BUTTON_IN_CATALOG).click()

    # кликаем на иконку тележки для перехода на страницу корзины
    browser.find_element(*CART_ICON).click()
    # проверяем что перешли на страницу корзины
    assert browser.current_url == CART_URL, 'url не соответствует ожидаемому'

    # кликаем на кнопку 'Checkout'
    browser.find_element(*CHECKOUT_BUTTON).click()

    # проверяем, что произошёл переход на первый шаг оформления заказа
    assert browser.current_url == CHECKOUT_STEP_1_URL, 'url не соответствует ожидаемому'

    # заполняем форму для оформления заказа
    browser.find_element(*FIRST_NAME_FIELD).send_keys(FIRST_NAME_VALUE)
    browser.find_element(*LAST_NAME_FIELD).send_keys(LAST_NAME_VALUE)
    browser.find_element(*POSTAL_CODE_FIELD).send_keys(POSTAL_CODE_VALUE)
    browser.find_element(*CHECKOUT_CONTINUE_BUTTON).click()

    # проверяем, что произошёл переход на второй шаг оформления заказа
    assert browser.current_url == CHECKOUT_STEP_2_URL, 'url не соответствует ожидаемому'

    browser.find_element(*CHECKOUT_FINISH_BUTTON).click()

    # проверяем, что произошёл переход на страницу подтверждения оформления заказа
    assert browser.current_url == CHECKOUT_COMPLETE_URL, 'url не соответствует ожидаемому'

    browser.find_element(*BACK_TO_PRODUCTS_BUTTON).click()

    # проверяем, что мы вернулись на страницу каталога
    assert browser.current_url == CATALOG_URL, 'url не соответствует ожидаемому'
