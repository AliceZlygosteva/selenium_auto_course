from selenium.webdriver.support.ui import Select
from locators import DROPDOWN_MENU, CATALOG_ITEM_NAME, CATALOG_ITEM_PRICE


def test_sorting_a_to_z(browser, auth):  # Проверка работоспособности фильтра (A to Z)
    # находим селект на странице каталога
    dropdown = browser.find_element(*DROPDOWN_MENU)

    #   создаём объект Select
    select = Select(dropdown)

    #  выбираем опцию из выпадающего списка по её атрибуту value
    select.select_by_value('az')

    #  находим все названия товаров в каталоге
    products = browser.find_elements(*CATALOG_ITEM_NAME)

    #  создаём список из названий товаров
    products_names = [product.text for product in products]

    #  сравниваем список товаров с отсортированной версией
    assert products_names == sorted(products_names), 'sort was not applied'


def test_sorting_z_to_a(browser, auth):  # Проверка работоспособности фильтра (Z to A)
    # находим селект на странице каталога
    dropdown = browser.find_element(*DROPDOWN_MENU)

    #   создаём объект класса Select
    select = Select(dropdown)

    #  выбираем опцию из выпадающего списка по её атрибуту value
    select.select_by_value('za')

    #  находим все названия товаров в каталоге
    products = browser.find_elements(*CATALOG_ITEM_NAME)

    #  создаём список из названий товаров
    products_names = [product.text for product in products]

    #  сравниваем список товаров с отсортированной версией
    assert products_names == sorted(products_names, reverse=True), 'sort was not applied'


def test_sorting_low_to_high(browser, auth):  # Проверка работоспособности фильтра (low to high)
    # находим селект на странице каталога
    dropdown = browser.find_element(*DROPDOWN_MENU)

    #   создаём объект класса Select
    select = Select(dropdown)

    #  выбираем опцию из выпадающего списка по её атрибуту value
    select.select_by_value('lohi')

    #  находим все цены товаров в каталоге
    products = browser.find_elements(*CATALOG_ITEM_PRICE)

    #  создаём список из цен товаров, преобразуя текст с ценой в число с плавающей точкой
    #  product.text[1:] предполагает, что первый символ в строке цены (символ валюты) пропускается
    products_prices = [float(product.text[1:]) for product in products]

    #  сравниваем список цен товаров с отсортированной версией
    assert products_prices == sorted(products_prices), 'sort was not applied'


def test_sorting_high_to_low(browser, auth):  # Проверка работоспособности фильтра (high to low)
    # находим селект на странице каталога
    dropdown = browser.find_element(*DROPDOWN_MENU)

    #   создаём объект класса Select
    select = Select(dropdown)

    #  выбираем опцию из выпадающего списка по её атрибуту value
    select.select_by_value('hilo')

    #  находим все цены товаров в каталоге
    products = browser.find_elements(*CATALOG_ITEM_PRICE)

    #  создаём список из цен товаров, преобразуя текст с ценой в число с плавающей точкой
    #  product.text[1:] предполагает, что первый символ в строке цены (символ валюты) пропускается
    products_prices = [float(product.text[1:]) for product in products]

    #  сравниваем список цен товаров с отсортированной версией
    assert products_prices == sorted(products_prices, reverse=True), 'sort was not applied'
