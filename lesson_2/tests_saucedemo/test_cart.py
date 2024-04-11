from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import CART_URL
from locators import (ADD_TO_CART_BUTTON_IN_CATALOG, ITEM_CATALOG_TITLE, ADD_TO_CART_BUTTON_IN_ITEM,
                      REMOVE_BUTTON_IN_ITEM, CART_ICON, CART_COUNTER, CART_ITEM, CART_REMOVE_BUTTON)


def test_add_to_cart_from_catalog(browser, auth):  # Добавление товара в корзину через каталог
    # кликаем на кнопку 'Add to cart'
    browser.find_element(*ADD_TO_CART_BUTTON_IN_CATALOG).click()

    # кликаем на иконку тележки для перехода на страницу корзины
    browser.find_element(*CART_ICON).click()

    # проверяем что перешли на страницу корзины
    assert browser.current_url == CART_URL, 'url не соответствует ожидаемому'

    wait = WebDriverWait(browser, 5)
    element = wait.until(EC.visibility_of_element_located(CART_ITEM))
    assert element is not None  # проверяем, что элемент с товаром присутствует


def test_delete_from_cart_via_cart(browser, auth):  # Удаление товара из корзины через корзину
    # кликаем на кнопку 'Add to cart'
    browser.find_element(*ADD_TO_CART_BUTTON_IN_CATALOG).click()

    # кликаем на иконку тележки для перехода на страницу корзины
    browser.find_element(*CART_ICON).click()

    # проверяем что перешли на страницу корзины
    assert browser.current_url == CART_URL, 'url не соответствует ожидаемому'

    #  кликаем на кнопку 'Remove'
    browser.find_element(*CART_REMOVE_BUTTON).click()

    # Проверяем, что товар был удален
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located(CART_ITEM))
        assert False, "Элемент с товаром не был удален"
    except:
        assert True


def test_add_to_cart_from_card(browser, auth):  # Добавление товара в корзину из карточки товара
    # кликаем на название товара для открытия карточки товара
    browser.find_element(*ITEM_CATALOG_TITLE).click()

    # кликаем на кнопку 'Add to cart' в карточке товара
    browser.find_element(*ADD_TO_CART_BUTTON_IN_ITEM).click()

    # кликаем на иконку тележки для перехода на страницу корзины
    browser.find_element(*CART_ICON).click()

    # проверяем что перешли на страницу корзины
    assert browser.current_url == CART_URL, 'url не соответствует ожидаемому'

    wait = WebDriverWait(browser, 5)
    element = wait.until(EC.visibility_of_element_located(CART_ITEM))
    assert element is not None  # проверяем, что элемент с товаром присутствует


def test_delete_from_cart_via_card(browser, auth):  # Удаление товара из корзины через карточку товара
    # кликаем на название товара для открытия карточки товара
    browser.find_element(*ITEM_CATALOG_TITLE).click()

    # кликаем на кнопку 'Add to cart' в карточке товара
    browser.find_element(*ADD_TO_CART_BUTTON_IN_ITEM).click()

    # Проверяем, что количество товаров в корзине увеличилось
    cart_badge = browser.find_element(*CART_COUNTER).text
    assert cart_badge == '1', 'Товар не добавлен в корзину'

    # кликаем на кнопку 'Remove'
    browser.find_element(*REMOVE_BUTTON_IN_ITEM).click()

    # Проверка, что кнопка меняется обратно на "Add to cart"
    add_to_cart_button_again = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(ADD_TO_CART_BUTTON_IN_ITEM))
    assert "Add to cart" in add_to_cart_button_again.text, "Товар не был удален из корзины"

    # Проверяем, что счётчика на иконке корзины нет
    wait = WebDriverWait(browser, 5)
    element_was_removed = wait.until(EC.invisibility_of_element_located(CART_COUNTER))
    assert element_was_removed, "Счётчик на иконке корзины все еще виден"
